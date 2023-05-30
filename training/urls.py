from django.urls import path

from training import views


urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('details/<str:id>', views.details, name='details'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete')
]
