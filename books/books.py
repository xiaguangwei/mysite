from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from books.models import Publisher, Book
from books.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

def book_form(request):
    return HttpResponse("hello books")

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q :
            error.append("Enter a search term.")
        elif len(q)> 5:
            error.append("Please enter at most 5 characters")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                  {'books': books,'query': q})
    return render_to_response('search_form.html', {'errors': error})

@csrf_exempt
def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
    else:
        form = ContactForm(
            initial={'subject':'I love your site!'}
        )
    return render_to_response('contact_form.html',{'form':form})
