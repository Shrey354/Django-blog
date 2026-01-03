from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post



def home(request):
    context = {
         'posts' : Post.objects.all()
    }
    return render(request,'post/post.html', context)

def about(request):
     return render(request,'post/about.html', {'title' : 'about'})

class PostListView(ListView):
     model = Post
     template_name = 'post/post.html'
     context_object_name = 'posts'
     ordering = ['-date_posted']

class PostDetailView(DetailView):
     model = Post
     template_name = 'post/post_detail.html'
