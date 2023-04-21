# -----------------------------------------------------------------------------------------------------------------

#                                         ( View, TemplateView , RedirectView )

#------------------------------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from .models import *
from app.models import Student

from django.views.generic.base import TemplateView, RedirectView
from django.views import View

from django.db.models import Q


# Create your views here.

def test(request):
    return render(request, "test.html")
#------------------------------------------------- View -----------------------------------------------------


# HttpResponse pass--------------------------------------------
class TestViewClass_1(View):
    def get(self, request):
        return HttpResponse(
            '<h1 style="text-align: center; color: red;">Her i pass HttpResponse</h1>'
            '<p style="text-align: center;" >Name: Md Rakib Hassan<p>'
            '<p style="text-align: center;" >Age: 27<p>'
            '<p style="text-align: center;" >Profession: Python with Django developer<p>'
            )
    

class TestViewClass_2(View):
    name = "Md Rakib Hassan"
    def get(self, request):
        return HttpResponse(
            self.name
            )  

    
class TestViewClass_3(View):
    #subject="Physics"
    subject=""
    def get(self, request):
        return HttpResponse(self.subject)
    

class SubClass(TestViewClass_2):
    def get(self, request):
        return HttpResponse(self.subject)
    

# Create a dictionary with multiple values
import json
class TestViewClass_3_1(View):
    name = "Md Rakib Hassan"
    subject="Python With Django"
    email = "rakib1515hassan@gmail.com"
    age = 27

    def get(self, request, *args, **kwargs):  
        data = {
            'name': self.name,
            'subject': self.subject,
            'email': self.email,
            'age': self.age,
            }
        # data = {
        #     'name': "Md Rakib Hassan",
        #     'subject': "Python With Django",
        #     'email': "rakib1515hassan@gmail.com",
        #     'age': 27,
        #     }
        # Convert dictionary to JSON string
        json_data = json.dumps(data)

        # Create an HttpResponse with the JSON string as content
        response = HttpResponse(json_data, content_type='application/json')
        return response
#----------------------------------------------------------------  


# HttpResponseRedirect  pass--------------------------------------------
# class TestViewClass_2_3(View):
#     name = "Md Rakib Hassan"
#     subject="Python With Django"
#     age = "27"
#     redirect_to = ''
#     def get(self, request):
#         # data = {
#         #     'name': self.name,
#         #     'subject': self.subject,
#         #     'age': self.age,
#         # }
#         # data = {
#         #     'name': "Md Rakib Hassan",
#         #     'subject': "Python With Django",
#         #     'age': 27,
#         # }
#         return HttpResponseRedirect(
#             data = {
#                 'name': self.name,
#                 'subject': self.subject,
#                 'age': self.age,
#                 }   
#             )  
#--------------------------------------------------------------------

# Class Base View----------------------------------------------------
class TestViewClass_4(View):
    # student_list={
    #     "name": "",
    #     "age": "",
    #     "study": "",
    # }
    def get(self, request):
        return render(request, "viewtest/test_1.html")
    
    def post(self, request):
        n=request.POST.get("name")
        a=request.POST.get("age")
        s=request.POST.get("study")
        # print("---------------------------------------")
        # print(f"Name: {n}, Age: {a}, Study: {s}")
        # print("---------------------------------------")

        student_Dictionary={
            "name": n,
            "age": a,
            "study": s,
        }

        return render(request, "viewtest/test_1.html", student_Dictionary)
    

class TestViewClass_5(View):
    student_name = []
    def get(self, request):
        data = {"std": self.student_name}
        return render(request, "viewtest/test_2.html", data)
    
    def post(self, request):
        n=request.POST.get("name")
        self.student_name.append(n)
        data = {"std": self.student_name}
        return render(request, "viewtest/test_2.html",data)
    

class TestViewClass_6(View):
    student_list={
        "name": "",
        "age": "",
    }
    def get(self, request):
        data = {"std": self.student_list}
        return render(request, "viewtest/test_3.html", data)
    
    def post(self, request):
        n=request.POST.get("name")
        a=request.POST.get("age")

        self.student_list["name"]=n
        self.student_list["age"]=a

        data = {"std": self.student_list}        

        return render(request, "viewtest/test_3.html",data)
        

class TestViewClass_7(View):
    
    def get(self, request):
        # data = {"std": self.student_list}
        return render(request, "viewtest/test_4.html")
    
    def post(self, request):
        student_list = {}
        key=request.POST.get("key")
        value=request.POST.get("value")
        print("------------------------------")
        print(key, value)
        print("------------------------------")
        # self.student_list.update({key : value})
        # Add the key-value pair to the dictionary
        student_list[key] = value
        print("------------------------------")
        print(student_list)
        print("------------------------------")

        # data = {"std": self.student_list}        

        return render(request, "viewtest/test_4.html",{
            "student_list": student_list
        })
    


class MyView(View):
    def get(self, request):
        # Render the form template
        return render(request, 'viewtest/test_5.html')

    def post(self, request):
        # Create an empty dictionary to store the key-value pairs
        my_dict = {}

        # Iterate over the submitted form data and add each key-value pair to the dictionary
        for key, value in request.POST.items():
            if key.startswith('key') and value:
                # Get the corresponding value for this key
                value_key = key.replace('key', 'value')
                value = request.POST.get(value_key)

                # Add the key-value pair to the dictionary
                my_dict[value] = value

        # Render a template that displays the contents of the dictionary
        return render(request, 'viewtest/test_5.html', {'my_dict': my_dict})

    
#---------------------------------------------------TemplateView----------------------------------------------------

# TemplateResponseMixin, ContextMixin, View
class templateview_1(TemplateView): 
    template_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Rakib'
        context['roll'] = 1515
        # print("---------------------------")
        # print(kwargs)
        # print("---------------------------")

        # context = {
        #     'name': "Rakib",
        #     'roll': 1515,
        # }
        return context


class templateview_2(TemplateView): 
    template_name = "viewtest/TemplateView_2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Rakib'
        context['roll'] = 1515

        # context = {
        #     'name': "Rakib",
        #     'roll': 1515,
        # }
        return context
    
class templateview_3(TemplateView): 
    template_name = "viewtest/TemplateView_3.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Student Class Import from app
        std = Student.objects.all()
        data = {
            'std': std
        }
        
        return data
    

class templateview_4(TemplateView): 
    template_name = "viewtest/TemplateView_4.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print("---------------------------")
        print(kwargs)
        print("---------------------------")
        s_id = kwargs['id']

        # Student Class Import from app
        std = Student.objects.get(id = s_id)
        data = {
            'std': std
        }
        
        return data

#---------------------------------------------------Redirect View----------------------------------------------------
class RedirectView_1(RedirectView): 
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)



class RedirectView_2(RedirectView):
    url="http://studentportal.diu.edu.bd/#/dashboard1" 
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    

class RedirectView_3(RedirectView):
    url="http://127.0.0.1:8000/gen/gen_1/" 
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    
class RedirectView_4(RedirectView):
    pattern_name = 'gen_1' 
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    
class RedirectView_5(RedirectView):
    pattern_name = ''
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class RedirectView_6(RedirectView): 
    pattern_name ="R_V"
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class R_V(TemplateView):
    template_name = "viewtest/Redirect_Result.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["name"] = "Md Rasel"
        data["Profesion"] = "Django Developer"

        # data = {
        #     "name": "Md Rasel",
        #     "Profesion": "Django Developer",
        # }

        return data
    

class RedirectView_7(RedirectView): 
    pattern_name ="R_V_2"
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class R_V_2(TemplateView):
    template_name = "viewtest/Redirect_Result_2.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["name"] = "Md Rasel"
        data["Profesion"] = "Django Developer"

        # data = {
        #     "name": "Md Rasel",
        #     "Profesion": "Django Developer",
        # }

        return data


# class RedirectView(RedirectView): 
#     pattern_name ="R_V"
#     #pattern_name = ""

#     ##permanent = False #By Deffault it's False this meen when redirect successfull then it return 302 code in consol
#     permanent = True #When it True then redirect successfull then it return 301 code in consol
#     query_string =True #By Deffault it's False

#     def get_redirect_url(self, *args, **kwargs):
#         return super().get_redirect_url(*args, **kwargs)
    



