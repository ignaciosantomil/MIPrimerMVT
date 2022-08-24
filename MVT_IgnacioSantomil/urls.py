
from django.contrib import admin
from django.urls import path
from familia.views import persona, ver_persona
urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar/', persona),
    path('verFamiliar/',ver_persona)
]
