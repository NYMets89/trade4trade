from django.urls import path
from . import views

urlpatterns = [
    # home/
    path('', views.home, name='home'),
    path('category/', views.categorypage, name='categorypage'),
    path('category/<int:category_id>', views.skillspage, name='skillspage'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/edit/<int:post_id>/<int:category_id>', views.edit, name='edit')
]