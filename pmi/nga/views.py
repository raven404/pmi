from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect, Http404
from .models import Post

# Create your views here.

def index(request):
    queryset = Post.objects.filter(featured=True)
    context= {
        'object_list':queryset
    }
    return render(request,'index.html', context)

def blog(request):
    return render(request,'blog.html', {})

def about(request):
    return render(request,'about.html', {})

def contact(request):
    return render(request,'contact.html', {})
