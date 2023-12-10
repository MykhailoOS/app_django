from .models import NavigationBar


def navigation_bar(request):
    items = NavigationBar.objects.filter(is_visible=True)
    return {'navigation_bar': items}
