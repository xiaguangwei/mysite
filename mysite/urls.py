"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_head, minute_head
from books.books import search_form, book_form , search, contact
from notes.notes import get_note_list, welcome,get_cagalogs

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_head),
    url(r'^minute/plus/(\d{1,2})/$', minute_head),
    url(r'^search_form/$', search_form),

    url(r'^notes/$', get_cagalogs),
    url(r'^book/$', book_form),
    url(r'^welcome/$', welcome),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
]
