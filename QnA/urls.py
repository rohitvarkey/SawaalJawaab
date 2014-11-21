from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$','QnA.views.home',name='home'),
        url(r'questions/(?P<questionId>[^/]+)/$','QnA.views.question_view',name='question_view'),
        url(r'questions/(?P<questionId>[^/]+)/fav/$','QnA.views.favourite_question',name='favourite_question'),
        url(r'questions/(?P<questionId>[^/]+)/upvote/$','QnA.views.upvote_question',name='upvote_question'),
        url(r'questions/(?P<questionId>[^/]+)/downvote/$','QnA.views.downvote_question',name='downvote_question'),
        url(r'topic/$','QnA.views.all_topics',name='all_topics'),
        url(r'topic/(?P<topicId>[^/]+)/$','QnA.views.topic_view',name='topic_view'),
        url(r'topic/(?P<topicId>[^/]+)/follow','QnA.views.follow_topic',name='follow_topic'),
        url(r'users/(?P<username>[^/]+)/$','QnA.views.user_profile',name='user_profile'),
        url(r'allUsers/','QnA.views.all_users_view',name='all_users_view'),
        url(r'base/','QnA.views.base_view',name='base'),
        url(r'signup/','QnA.views.signup',name='signup'),
        url(r'logout/','QnA.views.logout_view',name='logout_view'),
        url(r'addQuestion/','QnA.views.add_question',name='add_question'),
        url(r'comments/(?P<answerId>[^/]+)/$','QnA.views.add_comment',name='add_comment'),
        url(r'follow/(?P<username>[^/]+)/$','QnA.views.follow_user',name='follow_user'),
        url(r'feed/$','QnA.views.feed_view',name='feed_view'),
        url(r'search/$','QnA.views.search_view',name='search_view'),

)
