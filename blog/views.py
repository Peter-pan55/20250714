from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.forms import PostForm
from .models import Post

class PostListView(ListView): #CBV
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    #queryset = Post.objects.filter(published=True).order_by('-created_at')
    queryset=Post.objects.all().order_by('-created_at') #select * from Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list') # redirección tras crear

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')