from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls), # Dodane, może źle?
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('user_profile.urls')),
    path('stats/', include('hero_stats.urls')),
    path('fight/', include('fight.urls')),
    path('currencies/', include('currencies.urls')),
    path('inventory/', include('inventory.urls')),
    path('shop/', include('shop.urls')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]