from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    numfollowers = models.BigIntegerField(blank=True, default = 0) 
    def __str__(self):
        return self.user.username

class Answer(models.Model):
    author = models.ForeignKey('UserProfile')
    answerid = models.AutoField(primary_key=True)
    body = models.CharField(max_length=4000)
    createdTime = models.DateTimeField(auto_now_add=True)
    lastModTime = models.DateTimeField(auto_now=True)
    quesid = models.ForeignKey('Question')
    def __str__(self):
        return self.body[:20]

class Comment(models.Model):
    author = models.ForeignKey('UserProfile')
    commentid = models.AutoField(primary_key=True)
    body = models.CharField(max_length=4000)
    timeofcomment = models.DateTimeField(auto_now_add=True)
    ansid = models.ForeignKey('Answer')

class QuestionTopic(models.Model):
    question = models.ForeignKey('Question')
    topic = models.ForeignKey('Topic')
    qtid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.question.explanation + self.topic.name

class Topic(models.Model):
    topicid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Question(models.Model):
    author = models.ForeignKey('UserProfile')
    qid = models.AutoField(primary_key=True)
    explanation = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=1000)
    timeCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.explanation[:20]

class UserFavAnswer(models.Model):
    userid = models.ForeignKey('UserProfile')
    ansid = models.ForeignKey('Answer')
    ufaid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.userid.username + self.ansid.body[:20]

class UserFavQuestion(models.Model):
    userid = models.ForeignKey('UserProfile')
    qid = models.ForeignKey('Question')
    ufqid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.userid.username + self.qid.explanation[:20]

class UserFollowQuestion(models.Model):
    userid = models.ForeignKey('UserProfile')
    qid = models.ForeignKey('Question')
    ufqid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.userid.username + " " +self.qid.explanation[:20]

class UserFollowTopic(models.Model):
    user = models.ForeignKey('UserProfile')
    topic = models.ForeignKey('Topic')
    uftid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.user.username +" " +self.topic.name

class UserFollowUser(models.Model):
    follower = models.ForeignKey('UserProfile',related_name="follower")
    followed = models.ForeignKey('UserProfile',related_name="followed")
    ufuid = models.AutoField(primary_key=True)
    def __str__(self):
        return self.follower.firstName +"->"+ self.followed.firstName

class UserUpvoteQuestion(models.Model):
    user = models.ForeignKey('UserProfile')
    question = models.ForeignKey('Question')
    def __str__(self):
        return self.user.username + ":" + self.question.explanation[:20]

class UserDownvoteQuestion(models.Model):
    user = models.ForeignKey('UserProfile')
    question = models.ForeignKey('Question')
    def __str__(self):
        return self.user.username + ":" + self.question.explanation[:20]

class UserUpvoteAnswer(models.Model):
    user = models.ForeignKey('UserProfile')
    answer = models.ForeignKey('Answer')
    def __str__(self):
        return self.user.username + ":" + self.answer.body[:20]

class UserDownvoteAnswer(models.Model):
    user = models.ForeignKey('UserProfile')
    answer = models.ForeignKey('Answer')
    def __str__(self):
        return self.user.username + ":" + self.answer.body[:20]

class UserUpvoteComment(models.Model):
    user = models.ForeignKey('UserProfile')
    comment = models.ForeignKey('Comment')
    def __str__(self):
        return self.user.username + ":" + self.comment.body[:20]
