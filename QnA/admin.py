from django.contrib import admin
from QnA import models
# Register your models here.

admin.site.register(models.Answer)
admin.site.register(models.Comment)
admin.site.register(models.Question)
admin.site.register(models.QuestionTopic)
admin.site.register(models.Topic)
admin.site.register(models.UserFavAnswer)
admin.site.register(models.UserFavQuestion)
admin.site.register(models.UserFollowQuestion)
admin.site.register(models.UserFollowTopic)
admin.site.register(models.UserFollowUser)
admin.site.register(models.UserProfile)
