from django.shortcuts import render

# Create your views here.

def posts(request):
    return render(request, 'post/posts.html')

def create_post(request):
    return render(request, 'post/create_post.html')

def detail_post(request):
    return render(request, 'post/detail_post.html')

def delete_post(request):
    return render(request, 'post/delete_post.html')

def update_post(request):
    return render(request, 'post/update_post.html')