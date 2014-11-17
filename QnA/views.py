from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from QnA.models import *
from QnA.forms import *
# Create your views here.

def home(request):
    if request.user.is_authenticated():
        return redirect('user_profile',username=request.user.username)
    if request.method == 'GET':
        return render(request,'loginPage.html',{'failed':False})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('user_profile',username=username)#redirect to feed and not profile
            else:
                raise Http404
        else:
            return render(request,'loginPage.html',{'failed':True})
        return render(request,'loginPage.html')

def question_view(request,questionId):
    if request.method == 'GET':
        question = get_object_or_404(Question,qid=questionId)
        answers = Answer.objects.filter(quesid=questionId)
        topics = QuestionTopic.objects.filter(question=question)
        form = AnswerForm()
        return render(request,'question.html',{'question':question,
                                               'answers':answers,
                                               'topics':topics,
                                               'form':form,
                                               })
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            body = cleanedData['body']
            author = get_object_or_404(UserProfile,user=request.user)
            question = get_object_or_404(Question,qid=questionId)
            answer = Answer.objects.create(
                    author=author,
                    body=body,
                    quesid=question
                    )
            return redirect(
                    'question_view',
                    questionId=question.qid,
                    )

def user_profile(request,username):
    user = get_object_or_404(User,username=username)
    userProfile = get_object_or_404(UserProfile,user=user)
    return render(request,'userProfile.html',{'user':userProfile})

def topic_view(request,topicId):
    topic = get_object_or_404(Topic,topicid=topicId)
    questionTopicList = QuestionTopic.objects.filter(topicid=topicId)
    questions = []
    print questionTopicList
    if questionTopicList is None:
        raise Http404
    else:
        for questionTopic in questionTopicList:
            questions.append(Question.objects.get(qid=questionTopic.quesid.qid))
    print questions
    return render(request,'topic.html',{'questions':questions,'topic':topic})

def base_view(request):
    return render(request,'base.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        about = request.POST['about']
        try:
            user = User.objects.create_user(username,email,password)
            user = authenticate(username=username,password=password)
        except:
            raise Http404
        userProfile = UserProfile(user=user,firstName=firstName,lastName=lastName,about=about)
        userProfile.save()
        if user is not None:
            login(request,user)
        print "Redirecting"
        return redirect('user_profile',username=username)
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect("/")

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            explanation = cleanedData['explanation']
            body = cleanedData['body']
            author = get_object_or_404(UserProfile,user=request.user)
            question = Question(author=author,explanation=explanation,body=body)
            question.save()
            topics = cleanedData['topics'].split('\n')
            for topic in topics:
                topicObj, created = Topic.objects.get_or_create(name=topic)
                QuestionTopics.objects.create(question=question,topic=topicObj)
            return redirect('question_view',questionId=question.qid)
    else:
        form = QuestionForm()

    return render(request,'add_question.html', {
        'form':form
        })
