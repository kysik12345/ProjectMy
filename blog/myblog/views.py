from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    return render(request, template_name="myblog/index.html")

def index_blog(request):
    return render(request, template_name="myblog/index_blog.html")

def about(request):
    context = {
        "name": "Ivan",
        "lastname": "Ivanov",
        "email": "kysik1234@mail.ru",
        "title": "About"
    }
    return render(request, template_name="myblog/about.html", context=context)

def send_data(request):
    data = {"name": "Elena", "age": 16}
    return JsonResponse(data=data)

def add_post(request):
    if request.method == "GET":
        form = PostForm(author=request.user)
        context = {
            "form": form,
            'title': "Добавление поста"
        }
        return render(request, template_name='myblog/add_post.html', context=context)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            form.save()

        return index(request)



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': "Посты",
        'page_obj':page_obj
    }
    return render(request, template_name="myblog/posts.html", context=context)

def post_detail(request, slug):
    # post = Post.objects.get(slug=slug)
    post= get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Информация о посте',
        'post': post
    }
    return render(request, template_name='myblog/post_detail.html', context=context)
@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return post_list(request)
    else:
        form = PostForm()
        context = {
            'form': form,
            'title': "Редактировать пост"
        }
        return render(request, template_name="myblog/post_edit.html", context=context)
@login_required
def post_delete(request,pk):
    post= get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("myblog:post_list")
    return render(request, template_name="myblog/post_delete.html", context={'post:post'})

def page_not_found(request, exception):
    return render(request, 'myblog/404.html', status=404)

def server_error(request):
    return render(request, 'myblog/505.html', status=505)



