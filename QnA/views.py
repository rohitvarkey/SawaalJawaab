from django.shortcuts import render,get_object_or_404
from django.http import Http404
from QnA.models import *
# Create your views here.

def home(request):
    return render(request,'loginPage.html')

def question_view(request,questionId):
    question = get_object_or_404(Questions,qid=questionId)
    answers = Answers.objects.filter(quesid=questionId)
    return render(request,'question.html',{'question':question,
                                           'answers':answers})

def user_profile(request,username):
    user = get_object_or_404(User,name=username)
    return render(request,'userProfile.html',{'user':user})

def topic_view(request,topicId):
    topic = get_object_or_404(Topic,topicid=topicId)
    questionTopicList = QuestionTopic.objects.filter(topicid=topicId)
    questions = []
    print questionTopicList
    if questionTopicList is None:
        raise Http404
    else:
        for questionTopic in questionTopicList:
            questions.append(Questions.objects.get(qid=questionTopic.quesid.qid))
    print questions
    return render(request,'topic.html',{'questions':questions,'topic':topic})
