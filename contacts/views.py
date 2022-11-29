from django.http import HttpRequest  # HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView

from contacts.models import Contact
# from .forms import ContactForms
# from django.contrib import messages


# noinspection PyUnusedLocal
# def get_contacts(request: HttpRequest) -> HttpResponse:
#     contacts = Contact.objects.all()
#
#     return render(
#         request,
#         'contact_list.html',
#         {
#             'contacts': contacts
#         }
#     )


class ContactListView(ListView):
    model = Contact


def contact_details(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(
        request,
        'contacts/contact_details.html',
        {'contact': contact}
    )


class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'phone', 'date_of_birth', 'avatar')
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('contacts:index')


class ContactUpdate(UpdateView):
    model = Contact
    fields = ('name', 'phone', 'date_of_birth', 'avatar')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('contacts:index')


def contact_delete(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contacts:index')
