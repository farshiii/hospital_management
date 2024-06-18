from .models import Category


def mylink(request):
    links = Category.objects.all()
    return dict(links=links)
