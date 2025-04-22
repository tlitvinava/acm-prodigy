from django.core.management.base import BaseCommand
from main.models import Settings


class Command(BaseCommand):
    help = "Creating config variables, if they not exists"

    def handle(self, *args, **options):
        obj, _ = Settings.objects.get_or_create(name="configuration.olympiad.credentials")
        if _:
            obj.value='false'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.olymp.type")
        if _:
            obj.value='team'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="registration.team.available")
        if _:
            obj.value='false'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.registration.student_group")
        if _:
            obj.value='false'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.team.prefix")
        if _:
            obj.value='bsuir-open-'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.team.scope")
        if _:
            obj.value='number'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.solve.login")
        if _:
            obj.value='admin'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.solve.login")
        if _:
            obj.value='qwerty123'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.solve.url")
        if _:
            obj.value='https://solve.bsuir.by/api/v0'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.solve.event-feed.url")
        if _:
            obj.value='https://solve.bsuir.by/api/ccs/contests/{contest_id}/event_feed'
            obj.save()
            
        obj, _ = Settings.objects.get_or_create(name="configuration.agreement")
        if _:
            obj.value='true'
            obj.save()

        obj, _ = Settings.objects.get_or_create(name="configuration.agreement.url")
        if _:
            obj.value=''
            obj.save()
