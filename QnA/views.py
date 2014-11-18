import json
from itertools import chain
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
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

@login_required
def question_view(request,questionId):
    if request.method == 'GET':
        question = get_object_or_404(Question,qid=questionId)
        answers = Answer.objects.filter(quesid=questionId)
        topics = QuestionTopic.objects.filter(question=question)
        print topics
        form = AnswerForm()
        commentForm = CommentForm()
        userProf = UserProfile.objects.get(user=request.user)
        fav = UserFavQuestion.objects.filter(user=userProf).exists()
        for answer in answers:
            answer.comments = Comment.objects.filter(ansid=answer.answerid)
        return render(request,'question.html',{'question':question,
                                               'answers':answers,
                                               'topics':topics,
                                               'form':form,
                                               'commentForm':commentForm,
                                               'fav':fav,
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
@login_required
def user_profile(request,username):
    user = get_object_or_404(User,username=username)
    userProfile = get_object_or_404(UserProfile,user=user)
    currentUserProfile = get_object_or_404(UserProfile,user=request.user)
    follows = UserFollowUser.objects.filter(followed=userProfile,follower=currentUserProfile).exists()
    topics = UserFollowTopic.objects.filter(user=userProfile)
    questions = Question.objects.filter(author=userProfile).order_by('-timeCreated')
    answers = Answer.objects.filter(author=userProfile).order_by('-timeCreated')
    qna = sorted(
               chain(questions,answers),
                   key=lambda instance: instance.timeCreated,
                   reverse=True
                   )
    print qna 
    return render(request,'userProfile.html',{
        'curuser':userProfile,
        'follows':follows,
        'topics':topics,
        'qna':qna,
        })

def all_topics(request):
    topics = Topic.objects.all()
    return render(request,'allTopics.html',{
        'topics':topics
        })

@login_required
def topic_view(request,topicId):
    topic = get_object_or_404(Topic,topicid=topicId)
    questionTopicList = QuestionTopic.objects.filter(topic=topicId)
    questions = [] 
    currentUserProfile = get_object_or_404(UserProfile,user=request.user)
    follows = UserFollowTopic.objects.filter(user=currentUserProfile).exists()
    print questionTopicList
    if questionTopicList is None:
        raise Http404
    else:
        for questionTopic in questionTopicList:
            questions.append(Question.objects.get(qid=questionTopic.question.qid))
    print questions
    return render(request,'topic.html',
            {'questions':questions,
            'topic':topic,
            'follows':follows,
            })

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
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
@login_required
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
                QuestionTopic.objects.create(question=question,topic=topicObj)
            return redirect('question_view',questionId=question.qid)
    else:
        form = QuestionForm()

    return render(request,'add_question.html', {
        'form':form
        })
@login_required
def add_comment(request,answerId):
    form = CommentForm(request.POST)
    if request.method == 'GET' or not form.is_valid():
        raise Http404
    author = get_object_or_404(UserProfile,user=request.user)
    answer = get_object_or_404(Answer,answerid=answerId)
    body = form.cleaned_data['body']
    comment = Comment.objects.create(author=author,body=body,ansid=answer)
    return redirect("question_view",answer.quesid.qid)
@login_required
def upvote_question(request,questionId):
    question = get_object_or_404(Question,qid=questionId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Checking for downvote and resetting in case.
        downvote=UserDownvoteQuestion.objects.get(user=userProfile,question=question)
        downvote.delete()
    except:
        pass
    if UserUpvoteQuestion.objects.filter(user=userProfile,question=question).exists():
        UserUpvoteQuestion.objects.get(user=userProfile,question=question).delete()
    else:
        UserUpvoteQuestion.objects.create(user=userProfile,question=question)
@login_required
def downvote_question(request,questionId):
    question = get_object_or_404(Question,qid=questionId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Checking for upvote and resetting in case.
        upvote=UserUpvoteQuestion.objects.get(user=userProfile,question=question)
        upvote.delete()
    except:
        pass
    if UserDownvoteQuestion.objects.filter(user=userProfile,question=question).exists():
        UserDownvoteQuestion.objects.get(user=userProfile,question=question).delete()
    else:
        UserDownvoteQuestion.objects.create(user=userProfile,question=question)
@login_required
def upvote_answer(request,answerId):
    answer = get_object_or_404(Answer,answerid=answerId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Checking for downvote and resetting in case.
        downvote=UserDownvoteAnswer.objects.get(user=userProfile,answer=answer)
        downvote.delete()
    except:
        pass
    if UserUpvoteAnswer.objects.filter(user=userProfile,answer=answer).exists():
        UserUpvoteAnswer.objects.get(user=userProfile,answer=answer).delete()
    else:
        UserUpvoteAnswer.objects.create(user=userProfile,answer=answer)
@login_required
def downvote_answer(request,answerId):
    answer = get_object_or_404(Answer,answerid=answerId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Checking for upvote and resetting in case.
        upvote=UserUpvoteAnswer.objects.get(user=userProfile,answer=answer)
        upvote.delete()
    except:
        pass
    if UserDownvoteAnswer.objects.filter(user=userProfile,answer=answer).exists():
        UserDownvoteAnswer.objects.get(user=userProfile,answer=answer).delete()
    else:
        UserDownvoteAnswer.objects.create(user=userProfile,answer=answer)
@login_required
def upvote_comment(request,commentID):
    comment = get_object_or_404(Comment,id=commentID)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    """
    try:
        #Checking for downvote and resetting in case.
        downvote=UserDownvoteAnswer.objects.get(user=userProfile,answer=answer)
        downvote.delete()
    except:
        pass
    """
    if UserUpvoteComment.objects.filter(user=userProfile,
            comment=comment).exists():
        UserUpvoteComment.objects.get(user=UserProfile,
                comment=comment).delete()
    else:
        UserUpvoteComment.objects.create(user=userProfile,comment=comment)
@login_required
def favourite_question(request,questionId):
    question = get_object_or_404(Question,qid=questionId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Undo if present.
        favQuestion = UserFavQuestion.objects.get(user=userProfile,question=question)
        favQuestion.delete()
        print "Unfav"
        return HttpResponse(json.dumps({'fav':False}),
                content_type="application/json")
    except:
        UserFavQuestion.objects.create(user=userProfile,question=question)
        print "Fav"
        return HttpResponse(json.dumps({'fav':True}),
               content_type="application/json")

@login_required
def favourite_answer(request,answerid):
    answer = get_object_or_404(Answer,answerid=answerid)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Undo if present.
        favAnswer = UserFavAnswer.objects.get(user=userProfile,answer=answer)
        favAnswer.delete()
    except:
        UserFavAnswer.objects.create(user=userProfile,answer=answer)

@login_required
def follow_user(request,username):
    print request.user
    followedUser = get_object_or_404(User,username=username)
    followedUserProfile = get_object_or_404(UserProfile,user=followedUser)
    followerUserProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        #Undo if present.
        follow = UserFollowUser.objects.get(
                follower=followerUserProfile,
                followed=followedUserProfile,
                )
        print "Deleting"
        follow.delete()
        print "Deletion Successful"
        followers = len(UserFollowUser.objects.filter(followed=followedUserProfile))
        print "Returning response"
        return HttpResponse(
                json.dumps({
                    'follows':False,
                    'followers':followers,
                }),
            content_type="application/json")
    except:
        print "Creating"
        UserFollowUser.objects.create(
                follower=followerUserProfile,
                followed=followedUserProfile,
                )
        followers = len(UserFollowUser.objects.filter(followed=followedUserProfile))
        print followers
        return HttpResponse(
                json.dumps(
                    {'follows':True,
                    'followers':followers
                    }),
                    content_type="application/json")
@login_required
def follow_topic(request,topicId):
    topic = get_object_or_404(Topic,topicid=topicId)
    userProfile = get_object_or_404(UserProfile,user=request.user)
    try:
        topicFollow = UserFollowTopic.objects.get(
                topic=topic,
                user=userProfile,
                )
        topicFollow.delete()
        return HttpResponse(
                json.dumps({'follows':False}),
                content_type="application/json"
                )
    except:
        UserFollowTopic.objects.create(
                user=userProfile,
                topic=topic,
                )
        return HttpResponse(
                json.dumps({'follows':True}),
                content_type="application/json"
                )
