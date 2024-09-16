from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Posts.Status.PUBLISHED)




class Posts(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    
    class Status(models.TextChoices):
        DRAFT = ('DF', 'Draft')
        PUBLISHED = ('PB', 'Published')
    
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, default='This is a test')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    image = models.ImageField(upload_to='blogs', blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=Status,
        default=Status.DRAFT, 
        max_length=2)
    tags = TaggableManager() # the tags manager will allow to retrieve, add and remove tags from Posts objects
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        
    def comment_count(self):
        return self.comments.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[self.id,
                self.slug]
        )
        
class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering= ['-created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
        
class Message(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created = models.DateTimeField()
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return f'Message from {self.name} {self.last_name}'
        
class Subscriber(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = [
            '-subscribed_at'
        ]
        indexes = [
            models.Index(fields=['-subscribed_at'])
        ]
    def __str__(self):
        return f'{self.first_name} subscribed'
    