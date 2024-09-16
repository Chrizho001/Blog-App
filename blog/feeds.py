import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Posts
class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:blogs')
    description = 'New posts of my blog.'
    def items(self):
        return Posts.published.all()[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        html_content = markdown.markdown(item.body)
        return truncatewords(html_content, 30)  # Truncate after 30 words
    def item_pubdate(self, item):
        return item.publish