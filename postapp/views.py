from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserRegisterForm,PostForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.conf import settings
from django.core.mail import send_mail
from socialpost.settings import EMAIL_HOST_USER 


# Create your views here.
def base(request):

    return render(request ,'base.html')


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username =user.username,password =password)
            auth_login(request, new_user)
            return redirect('login')

    else:
        form = UserRegisterForm()


    context = {
        'form' : form
    }

    return render(request ,'postapp_temp/register.html',context)




def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }

    return render(request ,'postapp_temp/login.html',context)


@login_required(login_url = "/login")

def home(request):

    post = Post.objects.all()

    context ={
        'post':post
    }

    

    return render(request,'postapp_temp/home.html',context)


def addpost(request):
    
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            caption = form.cleaned_data['caption']
            description = form.cleaned_data['description']
            recipient_list = [request.user.email] 
            message = f"Caption:  {caption}\n\nDescription:  {description}"
            
            send_mail(
                subject= 'New Post Created',
                message= message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list= recipient_list
             )
            
            return redirect('home')

  

    context  = {"form":form}

    return render(request ,'postapp_temp/addpost.html',context)


def editpost(request,postid):

    post = get_object_or_404(Post, postid=postid)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'postid': postid
    }
    return render(request, 'postapp_temp/editpost.html', context)


def delete(request,postid):
  post=Post.objects.get(postid=postid)
  post.delete()
  return redirect('home')