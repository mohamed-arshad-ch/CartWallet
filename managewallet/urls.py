from django.urls import path
from .views import index,register,dash,logout,addproduct,viewproduct
urlpatterns = [
    path('',index,name="index"),
    path('register',register,name="register"),
    path('dash',dash,name="dash"),
    path('logout',logout,name="logout"),
    path('addproduct',addproduct,name="addproduct"),
    path('view/<int:id>/<str:ref>',viewproduct,name="viewproduct")
]