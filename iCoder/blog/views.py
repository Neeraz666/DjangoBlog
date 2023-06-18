from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    return render(request, "blog/bloghome.html", {'allPost': allPost})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comments':comments}
    return render(request, "blog/blogpost.html", context)

def blogComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, 'Your comment has been posted!')

    return redirect(f'/blog/{post.slug}')