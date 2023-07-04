from django.contrib import admin

from .models import Userprofile,Post,Like,Comment,Tag,Follow,Message,Group,GroupMembers

# Register your models here.

admin.site.register(Userprofile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(GroupMembers)