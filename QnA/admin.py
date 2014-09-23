from django.contrib import admin
from QnA import models
# Register your models here.

admin.site.register(models.Answers)
admin.site.register(models.Comments)
admin.site.register(models.User)
admin.site.register(models.Questions)
admin.site.register(models.QuestionTopic)
admin.site.register(models.Topic)
admin.site.register(models.UserFavAnswer)
admin.site.register(models.UserFavQuestion)
admin.site.register(models.UserFollowQuestion)
admin.site.register(models.UserFollowTopic)
admin.site.register(models.UserFollowUser)
