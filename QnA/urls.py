from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$','QnA.views.home',name='home'),
        url(r'questions/(?P<questionId>[^/]+)/$','QnA.views.question_view',name='question_view'),
        url(r'topic/(?P<topicId>[^/]+)/$','QnA.views.topic_view',name='topic_view'),
        url(r'users/(?P<username>[^/]+)/$','QnA.views.user_profile',name='user_profile'),
)
