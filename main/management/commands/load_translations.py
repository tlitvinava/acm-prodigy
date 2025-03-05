import os
import re
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings

from main.models import TranslationKey, Translation


class Command(BaseCommand):
    help = "Loading translations"

    __vars = set()

    def add_arguments(self, parser):
        parser.add_argument("config", type=Path)
        parser.add_argument("--force", action='store_true')
        parser.add_argument("--rewrite", action='store_true')

    def get_variables(self):
        reg = r'\{\{\s*tr\.(?P<name>[a-zA-Z\_0-9]*)(\s*\|\s[a-zA-Z0-9]*)*\s*\}\}'

        for root, dirs, files in os.walk(settings.TEMPLATE_DIR):
            for file in files:
                _file = Path(root, file)
                if _file.suffix == '.html':
                    with Path(_file).open('r+') as f:
                        text = f.read()
                        matches = re.findall(reg, text)
                        for match, _ in matches:
                            if match:
                                self.__vars.add(match)

    def handle(self, *args, **options):
        translations = None
        file = options['config']
        with Path(file).open('r') as f:
            translations = json.load(f)

        self.get_variables()

        for var in sorted(list(self.__vars)):
            if var not in translations.keys():
                print(f"[WARN] {var} is not specified")

        for key, langs in translations.items():
            if key not in self.__vars:
                continue
            tr_key, _ = TranslationKey.objects.get_or_create(key=key)
            for lang, value in langs.items():
                tr, _ = Translation.objects.get_or_create(
                    translation_key=tr_key,
                    language=lang
                )
                if isinstance(value, list):
                    text = '\n'.join(value)
                else:
                    text = value

                if _ or options['force']:
                    tr.translated_text = text
                tr.save()

        if options['rewrite']:
            unused = set(translations.keys()) - self.__vars

            for var in unused:
                del translations[var]

            with Path(file).open('w', encoding='utf-8') as f:
                print(json.dumps(translations, ensure_ascii=False), file=f)