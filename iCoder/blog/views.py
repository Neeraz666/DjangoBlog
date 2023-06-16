from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


def blogHome(request):
    allPost = Post.objects.all()
    return render(request, "blog/bloghome.html", {'allPost': allPost})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    context = {'post':post}
    return render(request, "blog/blogpost.html", context)
