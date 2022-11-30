from django.shortcuts import render, redirect,get_object_or_404
from .forms import ModelForm
from django.contrib import messages
from .models import Article, Comment
from .forms import ModelForm

# Create your views here.

def addcomment(request,id):
    article=get_object_or_404(Article, id=id)
    if request.method=="POST":
        yorumcu_adı =request.POST.get("yorumcu_adı")
        yorumcu_yorumu =request.POST.get("yorumcu_yorumu")

        Yeni_bir_yorum=Comment(yorumcu_adı=yorumcu_adı,yorumcu_yorumu=yorumcu_yorumu)
        Yeni_bir_yorum.article=article

        Yeni_bir_yorum.save()
        messages.success(request,"Yorum kaydedildi gülüm...")
    return redirect("/articles/detail/"+str(id))

def index(request):

    a_kelime =request.GET.get("a_kelime")
    
    if a_kelime:
        articles =Article.objects.filter(title__contains=a_kelime)
        return render(request,"index.html",{"articles":articles})
    articles =Article.objects.all()
    
    return render(request,"index.html",{"articles":articles})

def about(request):
    return render(request, "about.html")

    
def kontrol(request):

    articles =Article.objects.filter(author =request.user)
   # articles =get_object_or_404(Article, id=id)
    context ={
        "articles":articles
    }
    return render(request,"kontrol.html",{"articles":articles})

def addarticle(request):
    form =ModelForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article =form.save(commit =False)
        article.author =request.user 
        article.save()
        
        messages.success(request,"Makale Eklendi... Tebriklerr.")
        return redirect("index")
        
    return render(request,"addarticle.html",{"form":form})



def detail(request,id):
    
    yazı =get_object_or_404(Article, id=id)
    
    comments =yazı.deli.all()
    return render(request,"detail.html",{"yazı":yazı,"comments":comments})



def update(request,id):
    article= get_object_or_404(Article, id =id)
    form =ModelForm(request.POST or None,request.FILES or None, instance=article)
    if form.is_valid():
        article =form.save(commit =False)

        article.author =request.user 
        
        article.save()
        
        messages.success(request,"Güncelleme Başarılı reizz")
        return redirect("index")
   
    return render(request,"update.html",{"form":form})





def delete(request,id):
    silinecekyazı=get_object_or_404(Article,id=id)

    silinecekyazı.delete()
    messages.success(request,"Yazı Silindi... Tebriksss !!!")
    return redirect("article:kontrol")






