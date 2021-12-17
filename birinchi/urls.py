
from django.contrib import admin
from django.urls import path
from app1.views import take,take_ochir

urlpatterns = [
    path('admin/', admin.site.urls),
    path("take/",take,name='take'),
    path("take/<int:son>/",take_ochir),
]
