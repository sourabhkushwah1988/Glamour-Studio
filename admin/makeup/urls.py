from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inquire/', views.inquire, name='inquire'),
    path('makeup/', views.makeup, name='makeup'),
    path('makeup-data/', views.makeup_data, name='makeup_data'),
]
