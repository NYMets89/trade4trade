from django.urls import path
from . import views

urlpatterns = [
    # home/
    path('', views.home, name='home'),
    path('category/', views.categorypage, name='categorypage'),
    path('<int:category_id>/', views.skillspage, name='skillspage')
]