from django.contrib import admin

# Register your models here.
from .models import Link, Vote

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)