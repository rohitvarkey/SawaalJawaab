# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Answers(models.Model):
    author = models.CharField(max_length=30)
    answerid = models.BigIntegerField(primary_key=True)
    body = models.CharField(max_length=100, blank=True)
    timeofpost = models.DateTimeField()
    quesid = models.ForeignKey('Questions', db_column='quesid')
    authid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'answers'

class Comments(models.Model):
    author = models.CharField(max_length=30)
    commentid = models.BigIntegerField(primary_key=True)
    timeofcomment = models.DateTimeField()
    authorid = models.ForeignKey('User', db_column='authorid')
    ansid = models.ForeignKey(Answers, db_column='ansid')
    class Meta:
        managed = False
        db_table = 'comments'


class QuestionTopic(models.Model):
    quesid = models.ForeignKey('Questions', db_column='quesid')
    topicid = models.ForeignKey('Topic', db_column='topicid')
    qtid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'question_topic'

class Questions(models.Model):
    author = models.CharField(max_length=30)
    qid = models.BigIntegerField(primary_key=True)
    explanation = models.CharField(max_length=100, blank=True)
    body = models.CharField(max_length=100)
    time = models.DateTimeField()
    authorid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'questions'

class Topic(models.Model):
    topicid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'topic'

class User(models.Model):
    name = models.CharField(max_length=30)
    loginemail = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=10)
    numfollowers = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'user'

class UserFavAnswer(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    ansid = models.ForeignKey(Answers, db_column='ansid')
    ufaid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_fav_answer'

class UserFavQuestion(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    qid = models.ForeignKey(Questions, db_column='qid')
    ufqid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_fav_question'

class UserFollowQuestion(models.Model):
    userid = models.ForeignKey(User, db_column='userid')
    qid = models.ForeignKey(Questions, db_column='qid')
    ufqid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_follow_question'

class UserFollowTopic(models.Model):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    uftid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_follow_topic'

class UserFollowUser(models.Model):
    follower = models.ForeignKey(User,related_name="follower")
    followed = models.ForeignKey(User,related_name="followed")
    ufuid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_follow_user'
