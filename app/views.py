# -----------------------------------------------------------------------------------------------------------------

#                                         ( View, TemplateView , RedirectView )-CRUD

#------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from .models import *
#--------------------------------------------------------------------------
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# Class Base View----------------------------------------------------------
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.views.generic.list import ListView

# Create your views here.

def Home(request):
    return render(request, "home.html")


# -----------------------------CRUD--------------------------------------
class Home(View):
    def get(self, request):
        return render(request, "home.html")
    

class Student_View(TemplateView):
    template_name = "app/student_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #data['std'] = Student.objects.all()
        std = Student.objects.all()
        data ={
            "std": std,
        }
        return data

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        course = request.POST.get('course')

        std = Student()
        std.name = name
        std.roll = roll
        std.course = course
        std.save()
        return redirect("Student_View")
    
class DeleteStudent(RedirectView):
    #url = "http://127.0.0.1:8000/student/"
    # Redirect url(pattern_name)
    pattern_name = "Student_View"
    def get_redirect_url(self, *args, **kwargs):
        s_id = kwargs['id']
        std = Student.objects.get(id = s_id)
        std.delete()
        return super().get_redirect_url(*args)
    
class EditStudentView(View):
    def get(self, request, s_id):
        # print("-------------------------")
        # print(s_id)
        # print("-------------------------")
        std = Student.objects.all()
        std_edit = Student.objects.filter(id = s_id)
        # print("---------------------------------")
        # print("Editable Data: ",std_edit)
        # print("---------------------------------")

        data = {
            'std': std, 
            'std_edit': std_edit, 
        }
        return render(request, "app/student_list.html", data)
    
    def post(self, request, s_id):
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        course = request.POST.get('course')

        std = Student.objects.get(id = s_id)
        std.name = name
        std.roll = roll
        std.course = course
        std.save()
        return redirect("Student_View")
    


        
    








# class Student_View(ListView):
#     model = Student
    # For HTML "student_get.html"-------------------------------------------
    #template_name_suffix = "_get"
    # For Data Show Accending Order-----------------------------------------
    #ordering = ['name']
    # Rename html tamplate--------------------------------------------------
    #template_name = "home.html"
    # Rename Objects name---------------------------------------------------
    #context_object_name = "std"
    # def get_queryset(self):
    #     return Student.objects.filter(Q(course="Django") & Q(name="Rasel"))
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["teacher"] = Teacher.objects.all().order_by("name")
    #     return context




    
        
