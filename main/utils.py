from main.models import Settings


class Cfg:

    def __call__(self, name):
        try:
            cfg = Settings.objects.get(name=name)
        except Settings.DoesNotExist:
            cfg = Settings(name=name, value='')
            cfg.save()

        return cfg.value

Configuration = Cfg()