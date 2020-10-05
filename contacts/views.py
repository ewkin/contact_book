from django.shortcuts import render
from django.utils import timezone
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.filter()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
