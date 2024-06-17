from unicodedata import category
from django.views.generic import DetailView, ListView, TemplateView

from blog.models import Category, Post, Recipe


class HomeView(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': 'Home'}


class PostListView(ListView):


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs.get('slug')).name
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug']).select_related('category')


class PostDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Post.objects.get(slug=self.kwargs['slug']).title
        context['recipe'] = Recipe.objects.get(post__slug=self.kwargs['slug'])
        context['ingredients'] = context['recipe'].ingredients.split('\n')
        return context

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug']).select_related('category')
