import json
from pathlib import Path
from django.core.management.base import BaseCommand

from main.models import TranslationKey, Translation


class Command(BaseCommand):
    help = "Loading translations"

    def add_arguments(self, parser):
        parser.add_argument("config", type=Path)

    def handle(self, *args, **options):
        translations = None
        file = options['config']
        with Path(file).open('r') as f:
            translations = json.load(f)

        for key, langs in translations.values():
            tr_key, _ = TranslationKey.objects.get_or_create(key=key)
            for lang, value in langs.values():
                tr, _ = Translation.objects.get_or_create(
                    translation_key=tr_key,
                    language=lang
                )
                if isinstance(value, list):
                    text = '\n'.join(value)
                else:
                    text = value

                tr.translated_text = text
                tr.save()