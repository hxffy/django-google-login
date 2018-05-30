from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home),
    path('profile/', views.update_profile),
    path('account/logout', views.Logout),
]
