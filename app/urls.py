from django.urls import path
from app import views


urlpatterns = [
    path('registration/', views.reg),
    path('candidate/', views.can),
    path('adminshow/',views.show),
    path('adminreg/',views.admregistr),
    path('login/',views.loginn),
    path('show/',views.finall),
    path('home/',views.home),
    path('h/',views.h),
    path('voterlogin/',views.validation),
    path('candidateshow/',views.candshow),
    path("logout/", views.logout1)
]