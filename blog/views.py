from unicodedata import category
from django.views.generic import ListView, TemplateView

from blog.models import Post


class HomeView(TemplateView):
    template_name = 'base.html'


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['count'] = Post.objects.get(slug=self.kwargs['slug']).comment.count()

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug']).select_related('category')
