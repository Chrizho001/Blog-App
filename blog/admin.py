from django.contrib import admin
from .models import Posts, Comment, Message, Subscriber

# Register your models here.

# admin.site.register(Posts)

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'slug', 'author', 'publish', 'status', 'created', 'updated', 'image']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'message']
    list_filter = ['created', 'last_name', 'email', 'message']
    search_fields = [ 'message', 'email', 'last_name']
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subscribed_at']
    list_filter = ['subscribed_at', 'email']
    search_fields = ['last_name', 'first_name', 'email']