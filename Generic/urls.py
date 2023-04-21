from django.urls import path
from .views import *



urlpatterns = [
    path('gen/', GenericView, name="GenericView"),
    path('gen_1/', gen_1.as_view(), name="gen_1"),
    
    # path('gen_2/<int:pk>/', gen_2.as_view(), name="gen_2"),
    path('gen_2/<int:pk>/<str:slug>/', gen_2.as_view(), name="gen_2"), ## pk and slug কে একসাথে recive করার নিয়ম 
    # path('gen_2/<int:id>/', gen_2.as_view(), name="gen_2"),

    path('creat/', InsertPlayer.as_view(), name="InsertPlayer"),

    path('update/<int:pk>/', UpdatePlayer.as_view(), name="UpdatePlayer"),
    #path('update/<int:id>/', UpdatePlayer.as_view(), name="UpdatePlayer"),


    path('delete/<int:pk>/', DeletePlayer.as_view(), name="DeletePlayer"),

    path('delete_all/', DeleteAllPlayer.as_view(), name="DeleteAllPlayer"),
    #path('delete_all/', DeleteAllPlayer, name="DeleteAllPlayer"),


    

]