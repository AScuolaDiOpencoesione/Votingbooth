from django.core.management.base import BaseCommand, CommandError
from booth.models import * 
import requests

import csv
import io

to_copy = [21, 15, 119, 55, 42, 211, 18, 118, 126, 95, 67, 232, 179, 13, 91, 84, 100, 116, 193, 64, 192, 24, 134, 90, 65, 234, 207, 240, 110, 145]
_from = 2
_to = 3

class Command(BaseCommand):

    def handle(self, *args, **options):
        for tc in to_copy:
            ve = VotingElement.objects.get(session_id=_from, name=str(tc))
            ve.id = None
            ve.session_id=_to
            ve.save()
            print tc
        