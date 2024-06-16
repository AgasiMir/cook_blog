from django.views.generic import ListView, TemplateView

from blog.models import Post


class HomeView(TemplateView):
    template_name = 'base.html'


class PostListView(ListView):
    model = Post