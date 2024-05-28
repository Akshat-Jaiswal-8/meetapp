"""Module providing a function printing python version."""

from django.apps import AppConfig


class MeetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meetups'
