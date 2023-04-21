from django.urls import path
from .views import *



urlpatterns = [
    path('test/', test, name="test"),

# HttpResponse--------------------------------------------------------------------
    path('test-1/', TestViewClass_1.as_view(), name="TestViewClass_1"),

    path('test-2/', TestViewClass_2.as_view(), name="TestViewClass_2"),

    path('test-3/', TestViewClass_3.as_view(subject="Chemistry"), name="TestViewClass_3"),

    path('sub-t-2/', SubClass.as_view(), name="SubClass"),

    path('test-3-1/', TestViewClass_3_1.as_view(), name="TestViewClass_3_1"),

# Class base View --------------------------------------------------------------------
    path('test-4/', TestViewClass_4.as_view(), name="TestViewClass_4"),

    path('test-5/', TestViewClass_5.as_view(), name="TestViewClass_5"),

    path('test-6/', TestViewClass_6.as_view(), name="TestViewClass_6"),

    path('test-7/', TestViewClass_7.as_view(), name="TestViewClass_7"),

    path('test-8/', MyView.as_view(), name="MyView"),

#----------------------------------------------------Template View--------------------------------------------------------

    path('tv-1/', templateview_1.as_view( template_name="viewtest/TemplateView_1.html" ,extra_context ={'course': 'Django'}), name="templateview_1"), 
    path('tv-2/', templateview_2.as_view(extra_context ={'course': 'Django', 'fruit': 'Mango'}), name="templateview_2"), 
    path('tv-3/', templateview_3.as_view(), name="templateview_3"), 

    path('tv-4/<int:id>/', templateview_4.as_view(), name="templateview_4"),

#----------------------------------------------------Redirect View--------------------------------------------------------

    path('rd-1/', RedirectView_1.as_view(url="http://studentportal.diu.edu.bd/#/dashboard1"), name="RedirectView_1"),
    path('rd-2/', RedirectView_2.as_view(), name="RedirectView_2"),
    path('rd-3/', RedirectView_3.as_view(), name="RedirectView_3"),
    path('rd-4/', RedirectView_4.as_view(), name="RedirectView_4"),
    path('rd-5/', RedirectView_5.as_view(pattern_name = 'gen_1'), name="RedirectView_5"),

    path('rd-6/<int:id>/', RedirectView_6.as_view(), name="RedirectView_6"),
    path('rv-result/<int:id>/', R_V.as_view(extra_context ={'address': 'Saver'}), name="R_V"), 


    path('rd-7/<slug:product>/', RedirectView_7.as_view(), name="RedirectView_7"),
    path('rv-result-2/<slug:product>/', R_V_2.as_view(extra_context ={'address': 'Saver'}), name="R_V_2"),


    
    #path('rv-1/<int:id>/', RedirectView_1.as_view(), name="RedirectView_1"),
    #path('rv-5/', RedirectView.as_view(), name="RedirectView"),
    #path('rv-1/', RedirectView_1.as_view(pattern_name ="TestViewClass_1"), name="RedirectView_1"),

    # path('<slug:frute>/', templateview_1.as_view( template_name="test/TemplateView_1.html" ,extra_context ={'course': 'Django'}), name="templateview_rv"),
    path('rv-result/<int:id>/', R_V.as_view(extra_context ={'address': 'Saver'}), name="R_V"),
    #path('rv-result/', R_V.as_view(extra_context ={'address': 'Saver'}), name="R_V"),

]