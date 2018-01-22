from django.contrib import admin
from home.models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    # fields = ('title','desc','content',)
    class Media():
        js = ('/static/kindeditor/kindeditor-all-min.js',
              '/static/kindeditor/lang/zh-CN.js',
              '/static/kindeditor/config.js',
              )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
# admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)