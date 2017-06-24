
                
from django.core.management.base import BaseCommand, CommandError
from booth.models import * 
import requests

import csv
import io


class Command(BaseCommand):
    def handle(self, *args, **options):
        for u in User.objects.filter(username__icontains="_17"):
            ve = VoterElements.objects.get(voter=u)
            for vi in VotingElement.objects.filter(session=3):
                ve.items.add(vi)
                print "set",vi, "for",u
                
                