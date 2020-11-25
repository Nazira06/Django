from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def userlist(reguest):
    users = User.objects.all()
    return HttpResponse(users)

def bloglist(reguest):
    blogs = Post.objects.all()
    context = {'blogs':blogs}
    return render(reguest,'blog/post-template.html',context)



def post1list(reguest):
    posts = Post1.objects.all()
    context = {'blogs':posts}
    return render(reguest,'blog/post1-template.html',context)

