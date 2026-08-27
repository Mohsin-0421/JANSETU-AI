from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # This automatically redirects the empty root URL to your challenges API
    path('', RedirectView.as_view(url='/api/challenges/', permanent=False)), 
]