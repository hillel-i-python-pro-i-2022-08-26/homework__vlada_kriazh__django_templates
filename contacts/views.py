from django.http import HttpRequest  # HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


# def contact_new(request: HttpRequest):
#     if request.method == 'POST':
#         form = ContactForms(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.INFO, 'Contact added successfully')
#             return redirect('contacts:index')
#
#         else:
#             return render(
#                 request,
#                 'contacts/contact_create_form.html',
#                 {'form': form}
#             )
#     else:
#         form = ContactForms()
#         return render(
#             request,
#             'contacts/contact_create_form.html',
#             {'form': form}
#         )


# def contact_edit(request: HttpRequest, pk):
#     contacts = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         form = ContactForms(request.POST, instance=contacts)
#         if form.is_valid():
#             form.save()
#         return redirect('contacts:contact_details', pk=contacts.pk)
#     else:
#         form = ContactForms(instance=contacts)
#         return render(
#             request,
#             'contacts/contact_create_form.html',
#             {'form': form}
#         )


class ContactUpdate(UpdateView):
    model = Contact
    fields = ('name', 'phone', 'date_of_birth', 'avatar')
    template_name_suffix = '_update_form'


def contact_delete(request: HttpRequest, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contacts:index')
