from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from contacts.models import Contact


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
