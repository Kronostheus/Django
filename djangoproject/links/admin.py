from django.contrib import admin

# Register your models here.
from .models import Link, Vote, Comment

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vote, VoteAdmin)

