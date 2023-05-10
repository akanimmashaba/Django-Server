from django.shortcuts import render
from . forms import ContactForm
# Create your views here.




def contact_view(request):
    CONTACTS= {
    'address': '550 George Stow Street',
    'email':' info@jrco.co.za',
    'number': '+27 82 759 4079'

    }


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    form = ContactForm()
    context = {'form': form,
                'contacts': CONTACTS
               }
    return render(request, 'contact.html', context)