from django.urls import path
from . import views

urlpatterns = [
    # home/
    path('', views.home, name='home'),
    # blog/edit/<int:post_id>
#     path('edit/<int:post_id>', views.edit, name='edit'),
#     path('create/', views.create, name='create'),
]