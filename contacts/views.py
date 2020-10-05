from django.shortcuts import render
from django.utils import timezone
from .models import Contact
from django.shortcuts import render, get_object_or_404


def contact_list(request):
    contacts = Contact.objects.filter()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})
