from django.shortcuts import render
from .models import Contact
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def allcontact(request):
    contact = Contact.objects.all()
    context= {
        'contacts': contact
    }
    return render(request, 'index.html', context)


def formsubmit(request):
    # if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    newcontact = Contact.objects.create(name=name,email=email,phone=phone)
    newcontact.save()
    return HttpResponseRedirect('/')

def detailContact(request,pk):
    data = Contact.objects.get(id=pk)
    context = {
        "data":data
    }
    return render(request, 'detail.html', context)

def deleteContact(request,pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return HttpResponseRedirect('/')




