import logging
from django.core.management import BaseCommand, CommandParser
from contacts import models
from contacts.services import generate_contacts


class Command(BaseCommand):
    help = 'Generate contacts'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('django')

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            '--amount',
            type=int,
            default=10,
            help='Amount of generating contacts')

    def handle(self, *args, **options):
        amount: int = options['amount']
        self.logger.info(f"Generate {amount} contacts")

        current_amount = models.Contact.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        for number, contact in enumerate(generate_contacts(amount=amount), start=1):
            message = f"Generating contacts. {number}/{amount}."
            self.logger.info(f"{message} Start")
            contact.save()
            self.logger.info(f"{message} End")

        amount_after_generating = models.Contact.objects.all().count()
        self.logger.info(f"Amount of contacts after generating: {amount_after_generating}")
