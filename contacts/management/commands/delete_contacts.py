import logging
from django.core.management import BaseCommand, CommandParser
from contacts import models


class Command(BaseCommand):
    help = 'Delete contacts'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('django')

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            '--name',
            type=str,
            default='',
            help='Amount of generating contacts')

    def handle(self, *args, **options):
        name: str = options['name']

        current_amount = models.Contact.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        if name:
            query = models.Contact.objects.filter(name=name)
            total_amount, details = query.delete()
        else:
            query = models.Contact.objects.all()
            total_amount, details = query.delete()

        self.logger.info(f"Amount of deleted users: {total_amount}")

        amount_after_deleting = models.Contact.objects.all().count()
        self.logger.info(f"Amount of contacts after deleting: {amount_after_deleting}")
