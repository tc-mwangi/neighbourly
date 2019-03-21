from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseForbidden, HttpResponseServerError
from .models import Hood, Profile, Business
from .forms import ProfileForm, SearchForm
from django.contrib.auth.decorators import login_required
import datetime as dt



def edit_profile(request):
    '''display edit profile form

    Arguments:
        request {[type]} -- [description]
    '''

    render(request, 'main/edit_profile.html', {})


def user_profile(request):
    '''display user profile info

    Arguments:
        request {[type]} -- [description]
    '''
    form = ProfileForm

    render(request, 'main/user_profile.html', {"form":form})


def search_business(request):
    '''display search neighbourhood businesses form

    Arguments:
        request {[type]} -- [description]
    '''
    form = SearchForm

    render(request, 'main/search_business.html', {"form":form})


def business_listing(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''

    render(request, 'main/business_listing.html', {})


def hood_info(request):
    '''display search neighbourhood businesses form

    Arguments:
        request {[type]} -- [description]
    '''

    render(request, 'main/hood_info.html', {})


def hood_thread(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''

    render(request, 'main/hood_thread.html', {})





