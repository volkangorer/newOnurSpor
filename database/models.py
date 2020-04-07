from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Database(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    category = models.CharField(max_length = 50,verbose_name = "Kategori")
    position = models.CharField(max_length = 50,verbose_name = "Pozisyon")
    name = models.CharField(max_length = 50,verbose_name = "İsim")
    age = models.CharField(max_length = 50,verbose_name = "Yaş")
    size = models.CharField(max_length = 50,verbose_name = "Boy")
    weight = models.CharField(max_length = 50,verbose_name = "Kilo")
    foot = models.CharField(max_length = 50,verbose_name = "Kullandığı Ayak")
    club_history = models.CharField(max_length = 50,verbose_name = "Kulübe Katılma Tarihi")
    hoca_gorüsü = models.TextField()
    player_image = models.FileField(blank=True, null=True,verbose_name="Fotoğraf Ekleyin")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['-age']

class Galeri(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    galeri_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    galeri_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    galeri_content = models.FileField(blank=True, null=True,verbose_name="Fotoğraf Ekleyin")
    galeri_content2 = models.FileField(blank=True, null=True,verbose_name="Video Ekleyin")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.galeri_title

class Duyuru(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    duyuru_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    duyuru_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    duyuru_content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.duyuru_title

class Haber(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    haber_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    haber_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    haber_image = models.FileField(blank=True, null=True,verbose_name="Fotoğraf veya Video Ekleyin")
    haber_content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.haber_title

class Puan_Durumu(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    puan_category = models.CharField(max_length = 50,verbose_name = "Kategori")
    puan_link = models.CharField(max_length = 50,verbose_name = "Link")

    def __str__(self):
        return self.puan_category


class Club_information(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    club_title = models.CharField(max_length = 50,verbose_name = "Başlık")
    club_content = RichTextField(verbose_name = "İçerik")

    def __str__(self):
        return self.club_title

class Hakkimizda(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")

    def __str__(self):
        return self.title

class SporOkulu(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")

    def __str__(self):
        return self.title

class Basarilarimiz(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")

    def __str__(self):
        return self.title

