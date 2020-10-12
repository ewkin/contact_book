from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Contact
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


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


def register(request):
    if request.method == 'POST':

        # Assigning the User Creation form with the Post request object to form variable
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Getting the values from the form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate user using the authenticate method
            user = authenticate(username=username, password=raw_password)

            # After Successfully Authenticated then use login function to login the user

            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
