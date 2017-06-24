from django.core.management.base import BaseCommand, CommandError
from booth.models import * 
import requests

import csv
import io


file = "Associazioni.csv"

class Command(BaseCommand):

    def handle(self, *args, **options):
        u_t = {}
        for u in User.objects.all():
            u_t[u.username] = []
        with open(file, "rb") as f:
            reader = csv.DictReader(f, delimiter=";")
            for r in reader:
                u_t[r["utente"]].append(r["id_asoc"])
        
        print u_t
        
        for u in u_t:
            if len(u_t[u]) > 0:
                ve = VoterElements.objects.get(voter__username=u)
                for i in u_t[u]:
                    print i
                    vi = VotingElement.objects.get(session=2, name=i)
                    ve.items.add(vi)
                
                