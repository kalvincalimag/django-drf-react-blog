from django.contrib import admin
from api.models import CustomUser, Profile, Category, Comment, Post, Notification, Bookmark

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Bookmark)



