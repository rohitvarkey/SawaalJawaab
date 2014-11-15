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

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Comments(models.Model):
    author = models.CharField(max_length=30)
    commentid = models.BigIntegerField(primary_key=True)
    timeofcomment = models.DateTimeField()
    authorid = models.ForeignKey('User', db_column='authorid')
    ansid = models.ForeignKey(Answers, db_column='ansid')
    class Meta:
        managed = False
        db_table = 'comments'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Message(models.Model):
    messageid = models.BigIntegerField(primary_key=True)
    senderid = models.ForeignKey('User', db_column='senderid')
    recvid = models.ForeignKey('User', db_column='recvid')
    body = models.CharField(max_length=150)
    class Meta:
        managed = False
        db_table = 'message'

class Notifs(models.Model):
    notifid = models.BigIntegerField(primary_key=True)
    answernotifflag = models.IntegerField(blank=True, null=True)
    answerid = models.ForeignKey(Answers, db_column='answerid', blank=True, null=True)
    qsnotifflag = models.IntegerField(blank=True, null=True)
    quesid = models.ForeignKey('Questions', db_column='quesid', blank=True, null=True)
    commentnotifflag = models.IntegerField(blank=True, null=True)
    commentid = models.ForeignKey(Comments, db_column='commentid', blank=True, null=True)
    follownotifflag = models.IntegerField(blank=True, null=True)
    followid = models.ForeignKey('User', db_column='followid', blank=True, null=True)
    messagenotifflag = models.IntegerField(blank=True, null=True)
    messageid = models.ForeignKey(Message, db_column='messageid', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'notifs'

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
    follower = models.ForeignKey(User)
    followed = models.ForeignKey(User)
    ufuid = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'user_follow_user'

