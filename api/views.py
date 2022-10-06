from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.http import HttpResponseRedirect, HttpResponse
from .contactForm import ContactForm
# Create your views here.

def allcontact(request):
    contact = Contact.objects.all()
    context= {
        'contacts': contact
    }
    return render(request, 'index.html', context)

def formsubmit(request):
    form =ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    

# def formsubmit(request):
#     # if request.method == 'POST':
#     name = request.POST['name']
#     email = request.POST['email']
#     phone = request.POST['phone']

#     newcontact = Contact.objects.create(name=name,email=email,phone=phone)
#     newcontact.save()
#     return HttpResponseRedirect('/')

def updateContact(request,pk):
    data = get_object_or_404(Contact,id = pk)
    # name = request.POST['name']
    # email = request.POST['email']
    # phone = request.POST['phone']
    form = ContactForm(request.POST or None, instance=data)
    print(data) 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context = {
        "data":form,
    }
    return render(request, 'detail.html', context)

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




