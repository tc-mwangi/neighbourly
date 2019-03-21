
from django.conf.urls import url
from hood import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.edit_profile, name='edit_profile'),
    url('^profile/',views.user_profile, name='user_profile'),
    url('^search/',views.search_business, name='search_business'),
    url('^listing/', views.business_listing, name='business_listing'),
    url('^hood/info$', views.hood_info, name='hood_info'),
    url('^hood/thread$', views.hood_thread, name='hood_thread'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)