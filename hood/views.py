from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseForbidden, HttpResponseServerError
from .models import Hood, Profile, Business, locations, Health, Police
from .forms import ProfileForm, BusinessForm
from django.contrib.auth.decorators import login_required
import datetime as dt


def index(request):
    '''display introduction page

    Arguments:
        request {[type]} -- [description]
    '''
    
    return render(request, 'main/index.html', {})



def edit_profile(request):
    '''display edit profile form

    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'main/edit_profile.html', {})


def user_profile(request):
    '''display user profile info

    Arguments:
        request {[type]} -- [description]
    '''
    form = ProfileForm

    return render(request, 'main/profile.html', {"form":form})


def search_business(request):
    '''display search neighbourhood businesses form

    Arguments:
        request {[type]} -- [description]
    '''
    form = SearchForm

    return render(request, 'main/search.html', {"form":form})


def business_listing(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'main/business_listing.html', {})


def hood_info(request):
    '''display search neighbourhood businesses form

    Arguments:
        request {[type]} -- [description]
    '''

    return render(request, 'main/hood_info.html', {})

@login_required(login_url='/accounts/login')
def hood_thread(request):
    '''displays neighbourhood business listings

    Arguments:
        request {[type]} -- [description]
    '''
    


    return render(request, 'main/hood_thread.html', {})


@login_required
def feed(request):
    '''
    Items pinned by the people you follow
    '''
    enricher = Enrich(request.user)
    context = RequestContext(request)
    feed = feed_manager.get_news_feeds(request.user.id)['timeline']
    if request.POST.get('delete'):
        feed.delete()
    activities = feed.get(limit=25)['results']
    context['activities'] = enricher.enrich_activities(activities)
    response = render_to_response('main/feed.html', context)
    return response




