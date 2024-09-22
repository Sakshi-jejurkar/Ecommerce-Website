from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    context={
        'variable1': 'this is sent',
        'variable2': 'konnichiwa'
    }
    return render(request, 'index.html', context)
   # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse( "this is aboutpage")


def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Create an instance of the Contact model
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        
        # Save the instance
        contact.save()  # This should be contact.save(), not Contact.save()

        

    return render(request, 'contact.html')


    

    #return HttpResponse("this is contactpage")
