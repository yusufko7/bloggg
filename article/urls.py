
from django.urls import path
from article import views
app_name="article"


urlpatterns = [
    path('kontrol/', views.kontrol,name="kontrol"),
    path("addarticle/",views.addarticle,name="addarticle"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete, name="delete"),
    path("comment/<int:id>",views.addcomment, name="comment"),
   
]
