from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


def blogHome(request):
    allPost = Post.objects.all()
    context = {"allPost": allPost}
    return render(request, "blog/bloghome.html", context)


def blogPost(request, slug):
    return render(request, "blog/blogpost.html", {"slug": slug})
