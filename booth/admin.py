from django.contrib import admin

# Register your models here.


from .models import * 

class VCA(admin.ModelAdmin):
    list_filter = ("session", "user","item")

admin.site.register(VotingSession)
admin.site.register(VotingItem)
admin.site.register(VoteCast, VCA)
admin.site.register(VotingElement)
admin.site.register(VoterElements)
