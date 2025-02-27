from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from myapp.forms import *  # Ensure you import your forms
from myapp.models import *  # Ensure you import your model
 

def index(request):
    return render(request, 'index.html')

def home(request):
    # Fetch creators and their blogs
    creators = register.objects.filter(reg_type='Creator')  
    blogs_by_creator = {creator: blogs.objects.filter(author_name=creator.username) for creator in creators}
    return render(request, 'home.html', {'blogs_by_creator': blogs_by_creator})

def user_blogs(request, username):
    # Fetch the specific user and their blogs
    user = get_object_or_404(register, username=username, reg_type='Creator')
    user_blogs = blogs.objects.filter(author_name=user.username )
    return render(request, 'user_blogs.html', {'user': user, 'user_blogs': user_blogs})

    # return render(request, 'home.html')

def popular(request):
    return render(request, 'popular.html')

def search(request):
    return render(request, 'search.html')

def base(request):
    return render(request, 'base.html')

# def search_results(request):
#     query = request.GET.get('query', '').strip()
#     filter_by = request.GET.get('filter', 'title')  # Default to 'title' if no filter is selected
#     results = None

#     if query:
#         if filter_by == 'title':
#             results = Blog.objects.filter(title__icontains=query)
#         elif filter_by == 'author':
#             results = Blog.objects.filter(author__icontains=query)
#         elif filter_by == 'keywords':
#             results = Blog.objects.filter(keywords__icontains=query)

#     return render(request, 'search.html', {
#         'query': query,
#         'filter_by': filter_by,
#         'results': results
#     })
