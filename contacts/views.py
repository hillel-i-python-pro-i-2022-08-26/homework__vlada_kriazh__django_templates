from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact
from .forms import ContactForms
from django.contrib import messages


# noinspection PyUnusedLocal
def get_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()

    return render(
        request,
        'contacts.html',
        {
            'contacts': contacts
        }
    )


def contact_details(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(
        request,
        'contacts_crud/contact_details.html',
        {'contact': contact}
    )


def contact_new(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Contact added successfully')
            return redirect('contacts:index')

        else:
            return render(
                request,
                'contacts_crud/contact_new.html',
                {'form': form}
            )
    else:
        form = ContactForms()
        return render(
            request,
            'contacts_crud/contact_new.html',
            {'form': form}
        )


def contact_edit(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForms(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        return redirect('contacts:contact_details', pk=contact.pk)
    else:
        form = ContactForms(instance=contact)
        return render(
            request,
            'contacts_crud/contact_new.html',
            {'form': form}
        )


def contact_delete(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contacts:index')
