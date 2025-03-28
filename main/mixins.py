from django.shortcuts import render
from main.models import Translation


class LanguageMixin:

    def get_user_language(self, request):
        user_language = request.GET.get('lang') or request.session.get('language', 'ru')

        if user_language:
            request.session['language'] = user_language

        return user_language

    def get_translations(self, language):
        translations = Translation.objects.filter(language=language)
        return {
            translation.translation_key.key: translation.translated_text
            for translation in translations
        }

    def render_page(self, request, template_name, context=None):
        if context is None:
            context = {}

        user_language = self.get_user_language(request)
        translations_dict = self.get_translations(user_language)

        _context = {
            'tr': translations_dict,
            'selected_language': user_language,
        }

        _context.update(context)
        return render(request, template_name, _context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if context is None:
            context = {}

        user_language = self.get_user_language(self.request)
        translations_dict = self.get_translations(user_language)

        _context = {
            'tr': translations_dict,
            'selected_language': user_language,
        }

        _context.update(context)
        return _context