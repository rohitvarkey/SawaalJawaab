from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$','QnA.views.home',name='home'),
        url(r'questions/(?P<questionId>[^/]+)/$','QnA.views.question_view',name='question_view'),
        url(r'questions/(?P<questionId>[^/]+)/fav/$','QnA.views.favourite_question',name='favourite_question'),
        url(r'topic/$','QnA.views.all_topics',name='all_topics'),
        url(r'topic/(?P<topicId>[^/]+)/$','QnA.views.topic_view',name='topic_view'),
        url(r'users/(?P<username>[^/]+)/$','QnA.views.user_profile',name='user_profile'),
        url(r'base/','QnA.views.base_view',name='base'),
        url(r'signup/','QnA.views.signup',name='signup'),
        url(r'logout/','QnA.views.logout_view',name='logout_view'),
        url(r'addQuestion/','QnA.views.add_question',name='add_question'),
        url(r'comments/(?P<answerId>[^/]+)/$','QnA.views.add_comment',name='add_comment'),
        url(r'follow/(?P<username>[^/]+)/$','QnA.views.follow_user',name='follow_user'),

)
