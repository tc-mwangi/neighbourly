from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseForbidden, HttpResponseServerError
from .models import Hood, Profile, Business, UpdateHood, Post
from .forms import EditProfileForm, ChangeHoodForm, AddBusinessForm, PostForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User





def landing(request):
    '''display navigation options and pick a neighbourhood to join

    Arguments:
        request {[type]} -- [description]
    '''
    
    return render(request, 'main/landing.html', {})


def index(request):
    '''display navigation options and pick a neighbourhood to join

    Arguments:
        request {[type]} -- [description]
    '''
    
    return render(request, 'main/index.html', {})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    '''display edit profile form

    Arguments:
        request {[type]} -- [description]
    '''
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('user_profile')
    else:
        form = EditProfileForm()
    return render(request, 'main/edit_profile.html', {"form":form})


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    business = Business.get_profile_business(profile.id)
    title = f'@{profile.username}'
    return render(request, 'main/profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'business': business})


@login_required(login_url='/accounts/login/')
def join(request, hood_id):
    '''
    This view function will implement adding 
    '''
    hood = Hood.objects.get(pk=hood_id)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).update(hood_id=hood)
    else:

        Join(user_id=request.user, hood_id=hood).save()

    return redirect('index')


@login_required(login_url='/accounts/login/')
def add(request):

    current_user = request.user


    if request.method == 'POST':
        form = ChangeHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user_profile = current_user
            hood.save()
        return redirect('index')

    else:
        form = ChangeHoodForm()
    return render(request, 'main/add.html', {"form": form})




@login_required(login_url='/accounts/login/')
def add_business(request):
    '''display user profile info

    Arguments:
        request {[type]} -- [description]
    '''
    form = AddBusinessForm

    return render(request, 'main/add_business.html', {"form":form})


def search_business(request):
    '''display search neighbourhood businesses form

    Arguments:
        request {[type]} -- [description]
    '''
    

    return render(request, 'main/search.html', {})


def business_listing(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'main/business_listing.html', {})

def hood_listing(request):
    '''displays neighbourhood listings

    Arguments:
        request {[type]} -- [description]
    '''
    

    return render(request, 'main/hood_listing.html', {})



def hood_info(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Hood.objects.get(pk=request.user.join.hood_id.id)
            posts = Post.objects.filter(post_hood=request.user.join.hood_id.id)
            business = Business.objects.filter(
                business_hood=request.user.join.hood_id.id)
            return render(request, 'current_hood.html', {"hood": hood, "business": business, "posts": posts})
        else:
            hoods = Hood.get_all_hoods()
            return render(request, 'main/index.html', {"hoods": hoods})
    else:
        hoods = Hood.get_all_hoods()
        return render(request, 'main/index.html', {"hoods": hoods})








@login_required(login_url='/accounts/login')
def hood_thread(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''
    


    return render(request, 'main/hood_thread.html', {})


@login_required(login_url='/accounts/login/')
def add_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.post_hood = request.user.join.hood_id
            post.save()
        return redirect('homepage')

    else:
        form = PostForm()
    return render(request, 'mail/add_post.html', {"form": form})




