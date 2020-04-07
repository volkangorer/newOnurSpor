from django import forms
from .models import Database,Galeri,Duyuru,Haber,Puan_Durumu,Club_information,Hakkimizda,SporOkulu,Basarilarimiz

class AddPlayerForm(forms.ModelForm):
    
    class Meta :
        model = Database
        fields = ["category","position","name","age","size","weight","foot","club_history","player_image"]
    
class AddGaleriForm(forms.ModelForm):

    class Meta:
        model = Galeri
        fields = ["galeri_category","galeri_title","galeri_content","galeri_content2"]

class AddDuyuruForm(forms.ModelForm):

    class Meta:
        model = Duyuru
        fields = ["duyuru_category","duyuru_title","duyuru_content"]
class AddHaberForm(forms.ModelForm):

    class Meta:
        model = Haber
        fields = ["haber_category","haber_title","haber_image","haber_content"]

class AddPuanDurumuForm(forms.ModelForm):

    class Meta:
        model = Puan_Durumu
        fields = ["puan_category","puan_link"]

class AddClub_informationForm(forms.ModelForm):
    class Meta:
        model = Club_information
        fields = ["club_title","club_content"]

class AddHakkimizdaForm(forms.ModelForm):
    class Meta:
        model = Hakkimizda
        fields = ["title","content"]

class AddSporOkuluForm(forms.ModelForm):
    class Meta:
        model = SporOkulu
        fields = ["title","content"]

class AddBasarilarimizForm(forms.ModelForm):
    class Meta:
        model = Basarilarimiz
        fields = ["title","content"]
