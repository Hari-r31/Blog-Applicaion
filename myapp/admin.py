from django.contrib import admin
from .models import *

class regAdmin(admin.ModelAdmin):
    list_display = ('username','password', 'reg_type')

admin.site.register(register, regAdmin)

class blogsadmin(admin.ModelAdmin):
    list_display = ('author_id', 'author_name','title', 'content')

admin.site.register(blogs, blogsadmin)
