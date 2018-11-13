from .models import Section


def wagtree(request):
    return {'sections': Section.objects.all()}
