import logging
from django.core.management import BaseCommand
from middleware_example import models


class Command(BaseCommand):
    help = 'Delete request data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('django')

    def handle(self, *args, **options):

        query = models.RequestData.objects.all()
        total_amount, details = query.delete()

        self.logger.info(f"Amount of deleted elements: {total_amount}")
