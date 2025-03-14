from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from . models import Post

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/posts.html', context)

# def create_post(request):
#     if request.method == 'POST':
#         Post.objects.create(
#             title = request.POST['title'],
#             content = request.POST['content']
#         )
#         return redirect('detail_post')  # 게시글 목록 페이지로 리디렉션 (URL name에 맞게 변경)

#     return render(request, 'post/create_post.html')  # 템플릿 파일명은 필요에 맞게 수정

def create_post(request):
    if request.method == 'POST':
        post = Post.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )
        return redirect(reverse('detail_post', args=[post.pk]))  # 게시글 목록 페이지로 리디렉션 (URL name에 맞게 변경)

    return render(request, 'post/create_post.html')  # 템플릿 파일명은 필요에 맞게 수정

def detail_post(request, pk):
    detail_post = Post.objects.get(id=pk)
    context = {
        'detail_post': detail_post
    }
    return render(request, 'post/detail_post.html', context)

def update_post(request, pk):
    update_post = Post.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        update_post.title = title
        update_post.content = content
        update_post.save()
        return redirect('detail_post', pk=update_post.pk)
    context = {
        'update_post': update_post
    }
    return render(request, 'post/update_post.html', context)

def delete_post(request):
    return render(request, 'post/delete_post.html')