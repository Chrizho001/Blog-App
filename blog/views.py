from django.shortcuts import render
from .models import Posts
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from taggit.models import Tag
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.views.generic import ListView
from .forms import  CommentForm, MessageForm, SubscriberForm
from datetime import datetime

current_month = datetime.now().month



# Create your views here.

def home_view(request):
    recent_posts = Posts.objects.annotate(num_comments=Count('comments'))
    form = SubscriberForm()
    return render(request, 'blog/home.html', {
        'recent_posts' : recent_posts,
        'form' : form,
        })
    

def post_list(request, tag_slug=None):
    post_list = Posts.published.annotate(num_comments=Count('comments', distinct=True)).order_by('-created')
    all_tags = Tag.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag]).order_by('-created')
        # post_list = post_list.annotate(num_comments=Count('comments'))
        
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
    # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page_number is out of range get last page of result
         # If page_number is out of range get last page of result
        posts = paginator.page(paginator.num_pages)
    return render(
    request,
    'blog/blogs.html',
    {
    'posts': posts,
    'tag': tag,
    'post_list': post_list,
    'all_tags' : all_tags,
    }
    )
    
    
# Class based view to list out blogs

# class BlogListView(ListView):
#     # queryset = Posts.published.all()
#     paginate_by=4
#     context_object_name= 'posts'
#     template_name='blog/blogs.html'

#     def get_queryset(self):
#         # Annotate each post with the number of comments
#         return Posts.objects.annotate(num_comments=Count('comments'))


def post_detail(request, id, post):
    post = get_object_or_404(Posts,
                             status = Posts.Status.PUBLISHED,
                             id = id,
                             slug=post,
                             
                             )
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True) # retrieve a python list of IDs for the tags of the current post
    similar_posts = Posts.published.filter(tags__in=post_tags_ids).exclude(id=post.id) # get all the post that contain any of these tags, excluding the current post itself
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3] # count the number of tags and order them
    
    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'comments' : comments,
        'form' : form,
        'similar_posts' : similar_posts,
        })




@require_POST # This decorator only allows Post requests for this view
def post_comment(request, post_id):
    post = get_object_or_404(Posts, id=post_id, status=Posts.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST) # the comment data sent from the post request
    if form.is_valid():
    # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
    # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
        return render(request, 'blog/comment.html', {
            'post' : post,
            'form' : form,
            'comment' : comment,
        })


def post_message(request):
    if request == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, 'blog/message.html',  {'form' : form})
       
def news_subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save() 
            return JsonResponse({'message': 'success'}, status=200)  # Success response
        else:
            return JsonResponse({'message': 'error'}, status=400)  # Return an error response if form is invalid
    else:
        form = SubscriberForm()  
        return render(request, 'blog/subscribe.html', {'form' : form})