from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DjangoUser, Post, Comment, UserAccount

# Register custom user model
admin.site.register(DjangoUser, UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('user_account', 'title', 'body', 'published_date')
    list_filter = ('published_date', 'title')
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_account', 'description', 'posted_date')
    list_filter = ('posted_date', 'user_account')

admin.site.register(Comment, CommentAdmin)

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','bio','created_at','updated_at')
    list_filter = ('user','updated_at')
    
admin.site.register(UserAccount, UserAccountAdmin)
    