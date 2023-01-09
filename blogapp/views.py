from unicodedata import category
from urllib import response
from django.shortcuts import render, get_object_or_404
from .models import Post
import requests
import json
API_KEY ='0e9468e8f6364465befd5ed4809bd80a'

# Create your views here.

def index(request):
    # all_posts = Post.newmanager.all()
    all_posts = Post.objects.all()
    return render(request,'index.html', {'posts' : all_posts })

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data ['articles']
    else:
        url =f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data ['articles']
    return render(request, 'home.html',{'articles':articles})
