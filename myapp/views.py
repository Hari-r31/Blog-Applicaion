from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import * 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    rform=registerForm()
    if request.method == 'POST':
        rform = registerForm(request.POST)
        if rform.is_valid():
            rform.save()
            return redirect('myapp:login')
        else :
            print(rform.errors)
            return HttpResponse(rform.errors)
    return render(request,'signup.html',{'rform':rform})


def loginu(request):
    lform = loginForm()
    if request.method == 'POST':
        lform = loginForm(request.POST)
        if lform.is_valid():
            un = lform.cleaned_data['username']
            ps = lform.cleaned_data['password']
            user = authenticate(request, username=un, password=ps)
            if user:
                login(request, user)
                return redirect('home')
            else:
                lform.add_error(None, 'Invalid username or password')  # Add error to the form
    return render(request, 'login.html', {'form': lform})  # Pass the form to the template

def author_dashboard(request):
    matter = blogs.objects.filter(author_id=request.user)  # Use request.user directly
    user_name = request.user.username  # Get the username
    return render(request, 'authordb.html', {'matter': matter, 'user_name': user_name})  # Combine context into one dictionary

def blog_add(request):
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Don't save yet, need to assign author
            blog.author_id = request.user  # Set author_id as the logged-in user
            blog.author_name = request.user.username  # Set author_name as the logged-in user's username
            blog.save() 
            return redirect('myapp:author_dashboard')
        else:
            print(form.errors)
    else:
        form = blogForm()
    return render(request, 'blog_add.html', {'form': form})

def blog_edit(request, id):
    data = get_object_or_404(blogs, id=id)
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('myapp:author_dashboard')  # Redirect back to the home page
    else:
        form = blogForm(instance=data)
    return render(request, 'blog_edit.html', {'form': form})

def blog_delete(request, id):
    data = get_object_or_404(blogs, id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('myapp:author_dashboard')
    
def account_details(request):
    try:
        data = register.objects.get(id=request.user.id)
        print(request.user.id)
    except register.DoesNotExist:
        data = None 
    return render(request, 'account_details.html', {'data': data})



def modify_account(request):
    if not request.user.is_authenticated:
        return redirect('myapp:login')
    try:
        user_profile = request.user
    except Exception:
        return redirect('myapp:account_details')

    if request.method == 'POST':
        form = ModifyAccountForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('myapp:account_details')
    else:
        form = ModifyAccountForm(instance=user_profile)

    return render(request, 'modify_account.html', {'form': form})

def delete_user(request, user_id):
    print(id)
    if request.method == 'POST':
        # user = get_object_or_404(User, id=user_id)
        user=register.objects.get(id=user_id)
        user.delete()
        messages.success(request, f"User {user.username} deleted successfully!")
        return redirect('myapp:author_list')  # Replace with the actual view name


def ulogout(request):
    logout(request)
    return redirect('home')

def author_list(request):
    data1 = register.objects.filter(reg_type='Creator')
    data2 = register.objects.filter(reg_type='Viewer')
    return render(request, 'author_list.html', {'data1': data1, 'data2': data2})













