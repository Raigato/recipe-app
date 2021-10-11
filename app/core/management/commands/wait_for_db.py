import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

WAIT_TIME = 1  # seconds


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(WAIT_TIME)

        self.stdout.write(self.style.SUCCESS('Database available!'))
