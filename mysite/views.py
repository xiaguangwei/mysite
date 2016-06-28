from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html="<html><body>it's now %s.</body></html>" % now
    return HttpResponse(html)
def hours_head(request, offset):
    try:
        offset = int(offset)
    except err:
        raise Http404()
    dt=datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html="<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)
def minute_head(requst ,offset):
    try:
        offset=int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(minutes=offset)
    t = Template("<html><body> in {{ minute }} minute(s), it will be {{ time }}.</body></html>")
    html = t.render(Context({'minute': offset,'time': dt}))
    return HttpResponse(html)



