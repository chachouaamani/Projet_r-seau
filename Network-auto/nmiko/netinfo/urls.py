from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('enableOspf1',views.enableOspf1,name='enableOspf1'),
]