from django.contrib import admin
from .models import Blog, Category
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'description','image', 'date' , 'user' )
    
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
