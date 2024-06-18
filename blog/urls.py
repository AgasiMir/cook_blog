from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('single_post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('tags/<slug:slug>/', views.TagsListView.as_view(), name='tags'),
]
