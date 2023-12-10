from .models import Features


def navigation_bar(request):
    items = Features.objects.filter(is_visible=True)
    return {'features': items}
