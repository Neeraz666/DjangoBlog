from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']

    if len(query)>78:
        allPost = Post.objects.none()
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPostAuthor = Post.objects.filter(author__icontains=query)
        allPost = allPostTitle.union(allPostContent, allPostAuthor)

    if allPost.count() == 0:
        messages.warning(request, "No search results found. Please check your query.")
         
    params = {"allPosts": allPost, 'query':query}
    return render(request, 'home/search.html', params)