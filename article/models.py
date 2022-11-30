from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title =models.CharField(max_length=200,verbose_name="Başlık")
    content =RichTextField()
    date =models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    image =models.FileField(blank =True,null=True,verbose_name="Fotoğraf Ekle")
    class Meta:
        ordering =["-date"]


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="deli",verbose_name="Makale")
    yorumcu_adı =models.CharField(max_length=20,verbose_name="İsim")
    yorumcu_yorumu=models.CharField(max_length=400,verbose_name="Yorum")
    yorumcu_date =models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    class Meta:
        ordering =["-yorumcu_date"]
