from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('technologies/<str:category>', views.get_technologies_by_category, name='get_home_technologies_by_category')
]