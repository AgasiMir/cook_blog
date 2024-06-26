from django.template import Library

from blog.models import Category


register = Library()


@register.inclusion_tag("blog/include/top_menu.html")
def get_categories():
    return {"list_category": Category.objects.all()}
