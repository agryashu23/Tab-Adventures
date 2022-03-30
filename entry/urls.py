from django.urls import path
from entry import views

urlpatterns = [
    path("plan",views.plan, name= "plan"),
    path("planm",views.planm, name= "planmanali"),
    path("okok",views.okok, name= "okok"),
    path("entry",views.entry, name= "entry"),
    path("about",views.about, name= "about"),
    path("mail",views.mail, name= "mail"),
    path("login",views.login, name= "login"),
    path("gallery",views.gallery, name= "gallery"),
    path("mail", views.mail, name="Confirmation "),
    
    
    ] 