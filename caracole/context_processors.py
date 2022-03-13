from taggit.models import Tag

from . import models


def wagtree(request):
    # TODO: cache
    return {
        "sections": models.Section.objects.all(),
        "tags": Tag.objects.all(),
        "articles": models.Article.objects.live().reverse(),
        "evenements": models.Evenement.objects.all(),
    }
