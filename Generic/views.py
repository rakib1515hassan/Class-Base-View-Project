# -----------------------------------------------------------------------------------------------------------------

#                       ( ListView, DetailView , CreateView, UpdateView, DeleteView )

#------------------------------------------------------------------------------------------------------------------

import os
from django.shortcuts import render, redirect
from .models import Player
#--------------------------------------------------------------------------
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

#------------------------------------------------------------------------
from django.views.generic.base import TemplateView, RedirectView
# Display View-----------------------------------------------------------
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Editing View-----------------------------------------------------------
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.

def GenericView(request):
    return render(request, "generic.html")
# +++++++++++++++++++++++++++++++++++Display View--( ListView, DetailView )++++++++++++++++++++++++++++++++++++++

# List View---------------------------------------------------------------
class gen_1(ListView):
    model = Player

    # For HTML "Player_gen.html"-------------------------------------------
    #template_name_suffix = "_list" # Default
    #template_name_suffix = "_gen"  # পরিবর্তন করতে চাইলে  _gen এর জায়গায় লিখতে হবে 

    # For Data Show Accending Order-----------------------------------------
    ordering = ['name']

    # Rename html tamplate--------------------------------------------------
    #template_name = "Generic/player_list.html" # Default
    # template_name = "gen_1.html"

    # Rename Objects name---------------------------------------------------
    #context_object_name = "player_list" #Default
    # context_object_name = "ply"

    ##For Filtering ------------------------------
    # def get_context_data(self, **kwargs):
    #     # data = super().get_context_data(**kwargs)

    #     ply = Player.objects.all()  

    #     #ply = Player.objects.filter(play = "Football") 
         
    #     #ply = Player.objects.filter(play = "Cricket", position = "Allrounder") 
     
    #     #ply = Player.objects.filter(Q(play="Cricket") | Q(play="Football"))  

    #     #ply = Player.objects.filter(Q(play="Cricket") & Q(age = 26 ))  
 
    #     data = {
    #         'ply': ply
    #     }         
    #     return data
    
    # def get_template_names(self):
    #     if self.request.COOKIES['user']=="Rakib":
    #         template_name = "rakib.html"
    #     else:
    #         template_name = "abc.html"
    #     return [template_name]
    
    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = "superuser.html"
    #     elif self.request.user.is_staff:
    #         template_name = "staff.html"
    #     else:
    #         template_name = "abc.html"
    #     return [template_name]


# class Student_View(ListView):              
#     model = Student                        
    # For HTML "student_get.html"-------------------------------------------
    # template_name_suffix = "_get"
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

# DetailView-----------------------------------------------------------------
class gen_2(DetailView):
    model = Player

    # For HTML "Player_gen.html"-------------------------------------------
    #template_name_suffix = "_gen"

    # Rename html tamplate--------------------------------------------------
    #template_name = "player_detail.html" # Default template
    # template_name = "gen_2.html"

    # Rename Objects name---------------------------------------------------
    #context_object_name = "player" # Default Object
    # context_object_name = "ply"

    # pk Override in id-----------------------------------------------------
    #pk_url_kwarg = 'id'

    #  যদি pk এবং slug দুটির মাধ্যমে data show করতে চাই
    # query_pk_and_slug = False # By Default
    query_pk_and_slug = True 

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)

        #data['all_player'] = Player.objects.all()
        data['all_player'] = self.model.objects.all()
        # all_player = Player.objects.all()
        # data = {
        #     "all_player": all_player,
        # }
        return data
    

# +++++++++++++++++++++++++++++++ Editing View ----( CreateView, UpdateView, DeleteView )+++++++++++++++++++++++++++++++++++++++++
# class InsertPlayer(View):
#     def get(self, request):
#         return render(request, "Generic/player_form.html")
        

class InsertPlayer(CreateView):
    model = Player

    # If you use django form
    #fields = ["name", "pic", "age", "play", "position"]

    # Template Rendaring Default template render it dose't need to mentios. Automatically it rediract this html
    #template_name = "Generic/player_form.html" # ( Default template render )

    #redirect to success page after form submission
    #success_url = "http://127.0.0.1:8000/gen/gen_1/"
    success_url = "/gen/gen_1/"

    def get(self, request):
        return render(request, "Generic/player_form.html")
    
    def post(self, request):
        try:
            ply = Player()
            ply.name = request.POST.get("name")
            p = request.FILES.get("pic")
            if p:
                ply.pic = p
            else:
                if len(request.FILES)!=0:
                    if len(ply.pic)>0:
                        os.remove(ply.pic.path)
                    ply.pic = p
            ply.age = request.POST.get("age")
            ply.play = request.POST.get("play")
            ply.position = request.POST.get("position")
        
            ply.save()

        #     # name = request.POST.get("name")
        #     # pic = request.FILES.get("pic")
        #     # age = request.POST.get("age")
        #     # play = request.POST.get("play")
        #     # position = request.POST.get("position")

        #     # Player(name=name, pic=pic, age=age, play=play, position=position).save()

            return redirect("gen_1")
        except:
            return HttpResponse("Please Fill Your Information.")
    



class UpdatePlayer(UpdateView):
    model = Player
    #fields = ["name", "pic", "age", "play", "position"]
    success_url = "/gen/gen_1/"

    #pk Override in id-----------------------------------------------------
    #pk_url_kwarg = 'pk' ## ( Default )
    #pk_url_kwarg = 'id'

    def get(self, request, pk):
        upd = Player.objects.get(id = pk)
        data = {
            "upd": upd,
        }
        return render(request, "Generic/player_form.html", data)
    
    def post(self, request, pk):
        upd = Player.objects.get(id = pk)
        upd.name = request.POST.get("name")
        p = request.FILES.get("pic")
        if p:
            if upd.pic:
                if len(request.FILES)!=0:
                    if len(upd.pic)>0:
                        os.remove(upd.pic.path)
                        upd.pic = p
            else:
                upd.pic = p
        upd.age = request.POST.get("age")
        upd.play = request.POST.get("play")
        upd.position = request.POST.get("position")
     
        upd.save()
        return redirect("gen_1")
    

class DeletePlayer(DeleteView):
    model = Player

    # This Class Demand a HTML tamplate, That name must be ( player_confirm_delete.html )
    # Because the method will be confirm that, are you actually delete this Yes or NO
    #template_name = "player_confirm_delete.html" ## ( Default Confermation Page )
    # template_name = "Your Template Location" 
    
    #success_url = '/gen/gen_1/'

    def post(self, request, pk):
        ply_delet = Player.objects.get(id = pk)
        if ply_delet.pic:
            if len(ply_delet.pic)>0:
                os.remove(ply_delet.pic.path)
                ply_delet.delete()
                print("---------------------------")
                print("get profil pic")
                print("---------------------------")
        else:
            ply_delet.delete()
            print("---------------------------")
            print("he/she has no profil pic")
            print("---------------------------")
        return redirect('gen_1')


class DeleteAllPlayer(View):
    def get(self, request):
        ply = Player.objects.all()
        for p in ply:
            if p.pic:
                if len(p.pic)>0:
                    os.remove(p.pic.path)
                p.delete()
            else:
                p.delete()
        return redirect('InsertPlayer')
    

