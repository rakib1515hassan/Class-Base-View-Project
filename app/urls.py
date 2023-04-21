from django.urls import path
from .views import *



urlpatterns = [
    path('', Home.as_view(), name="home"),
    
    path('student/', Student_View.as_view(), name="Student_View"),
    path('delete/<int:id>/', DeleteStudent.as_view(), name="DeleteStudent"),
    path('edit/<int:s_id>/', EditStudentView.as_view(), name="EditStudentView"),
    

]