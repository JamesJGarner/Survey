from django.contrib import admin
from .models import Poll, PollAnswer, Vote


class PollAnswerAdmin(admin.TabularInline):
    extra = 1
    model = PollAnswer

class VoteAdmin(admin.TabularInline):
    extra = 1
    model = Vote


class PollAdmin(admin.ModelAdmin):
    inlines = [PollAnswerAdmin, VoteAdmin]

admin.site.register(Poll, PollAdmin)
