from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Blog, Category
from .forms import BlogForm


def home(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'main/home.html', {'blogs': blogs}
)


def register(request):
    if request.method == 'GET':
        return render(request, 'main/register.html', {'form': UserCreationForm()})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account') 
            else:
                return render(request, 'main/register.html', {'form': UserCreationForm(), 'error': 'Failed to confirm password!'})
        except IntegrityError:
            return render(request, 'main/register.html', {'form': UserCreationForm(), 'error': 'This user already exists!'})
        except KeyError:
            return render(request, 'main/signup_user.html', {'form': UserCreationForm(), 'error': 'All fields must be filled in!'})



def loginUser(request):
    if request.method == 'GET':
        return render(request, 'main/loginUser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'main/loginUser.html', {'form': AuthenticationForm(), 'error': 'Invalid password or username.'})      


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



def account(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, 'main/account.html')

def account(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, 'main/account.html', {'blogs': blogs})


def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.image = request.FILES['image'] # имя поля для загрузки изображения
            new_blog.save()
            return redirect('account')
    else:
        form = BlogForm()
    return render(request, 'main/createBlog.html', {'form': form})


def changeBlog(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            if 'image' in request.FILES:
                blog.image = request.FILES['image']
            form.save()
            return redirect('account')
        else:
            return render(request, 'main/changeBlog.html', {'blog': blog, 'form': form, 'error': 'Ошибка'})
    else:
        form = BlogForm(instance=blog)
        return render(request, 'main/changeBlog.html', {'blog': blog, 'form': form})


def deleteBlog(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('account')


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'main/detail.html', {'blog': blog})


def blog(request):
    categories = Category.objects.all() 
    blogs = Blog.objects.all() 
    if request.method == 'POST': 
        category_id = request.POST.get('category_id') 
        category = get_object_or_404(Category, id=category_id) 
        blogs = Blog.objects.filter(categories=category) 
    return render(request, 'main/blog.html', {'categories': categories, 'blogs':blogs})

