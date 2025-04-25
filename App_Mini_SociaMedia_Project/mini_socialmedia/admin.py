from django.contrib import admin
from .models import Post, Comment, UserAccount

class PostAdmin(admin.ModelAdmin):
    list_display = ('user_account','title','body','published_date')   
    list_filter = ('published_date', 'title')
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_account','description','posted_date')
    list_filter =('posted_date','user_account')
admin.site.register(Comment,CommentAdmin)

admin.site.register(UserAccount)