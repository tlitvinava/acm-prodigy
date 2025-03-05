import json
from pathlib import Path
from django.core.management.base import BaseCommand

from main.models import TranslationKey, Translation


class Command(BaseCommand):
    help = "Dumping translations"

    def add_arguments(self, parser):
        parser.add_argument("config", type=Path)

    def handle(self, *args, **options):
        translations = {}
        file = options['config']

        for item in TranslationKey.objects.all():
            translations[item.key] = {}
            for trans in Translation.objects.filter(translation_key=item):
                translations[item.key][trans.language] = trans.translated_text

        with Path(file).open('w', encoding='utf-8') as f:
            print(json.dumps(translations, ensure_ascii=False), file=f)