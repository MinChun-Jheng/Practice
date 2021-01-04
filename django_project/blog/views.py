from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'admin',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'Jan 4, 2021'
    },
    {
        'author': 'admin',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'Jan 4, 2021'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
