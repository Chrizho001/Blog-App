import markdown
from django import template

register = template.Library()

from django.utils.safestring import mark_safe
import markdown
from django import template
from django.template.defaultfilters import truncatewords_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown_truncate')
def markdown_truncate(value, word_count):
    # Convert markdown to HTML
    html_content = markdown.markdown(value, extensions=['extra'])
    # Truncate the HTML content
    truncated_content = truncatewords_html(html_content, word_count)
    return mark_safe(truncated_content)


import markdown
from django.utils.safestring import mark_safe
@register.filter(name='markdown')
def markdown_format(text):
 return mark_safe(markdown.markdown(text))