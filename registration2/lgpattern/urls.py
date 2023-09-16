from django.urls import path
from . import views
urlpatterns=[
    path('m/',views.myfun,name="myfun"),
    path('k/',views.login,name="login"),
    path('y/',views.home,name="website"),
    path('',views.logout,name="logout"),
]