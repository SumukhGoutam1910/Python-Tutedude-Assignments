from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


# Home page: list all blogs
def home(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_home.html', {'blogs': blogs})

# User's own blogs
@login_required
def my_blogs(request):
    blogs = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'my_blogs.html', {'blogs': blogs})


# Create a new blog post (login required)
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('my_blogs')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})

# Edit a blog post (login required)
@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('my_blogs')
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

# Delete a blog post (login required)
@login_required
def delete_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('my_blogs')
    return render(request, 'delete_blog.html', {'blog': blog})
