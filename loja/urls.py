from django.contrib import admin
from django.urls import path, include

from comum.views import inicio


urlpatterns = [
    path('', inicio, name='inicio'),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('admin/', admin.site.urls),
]
