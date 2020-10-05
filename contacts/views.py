from django.shortcuts import render
from django.utils import timezone
from .models import Contact
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.shortcuts import redirect


def contact_list(request):
    contacts = Contact.objects.filter()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_new.html', {'form': form})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_new.html', {'form': form})
