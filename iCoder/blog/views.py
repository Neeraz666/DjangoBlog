from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("Welcome to Blog!")

def blogPost(request, slug):
    return HttpResponse(f"Welcome to BlogPost! {slug}")