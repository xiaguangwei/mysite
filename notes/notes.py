from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

from django.template import Template, Context
# Create your views here.

def get_note_list(request):
    return render_to_response('note_list.html')

def welcome(request):
    return HttpResponse("welcome")

def get_cagalogs(request):
    catalogs = ['File','Edit']
    return render_to_response('note_list.html',{'catalogs': catalogs})