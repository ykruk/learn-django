from django.contrib import admin
from .models import Post, Exposition, Post_img, Exposition_img, Message

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published_date')
    search_fields = ['author', 'title']
class ExpositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender', 'message')
class Exposition_imgAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_alt')
    search_fields = ['img_alt']
class Post_imgAdmin(admin.ModelAdmin):
    list_display = ('img', 'img_alt')
    search_fields = ['img_alt']

admin.site.register(Post, PostAdmin)
admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(Post_img, Post_imgAdmin)
admin.site.register(Exposition_img, Exposition_imgAdmin)
admin.site.register(Message, MessageAdmin)

# Register your models here.
