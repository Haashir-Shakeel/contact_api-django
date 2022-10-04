from django.shortcuts import render
from .models import Contact
# Create your views here.

def allcontact(request):
    contact = Contact.objects.all()
    context= {
        'contacts': contact
    }
    return render(request, 'index.html', context)



