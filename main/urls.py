from django.urls import path
from main.admin import payment_system_site


urlpatterns = [
    path("admin/", payment_system_site.urls),
]
