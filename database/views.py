
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import AddPlayerForm,AddGaleriForm,AddDuyuruForm,AddHaberForm,AddClub_informationForm,AddHakkimizdaForm,AddSporOkuluForm,AddBasarilarimizForm
from .models import Database,Galeri,Duyuru,Haber,Club_information,Hakkimizda,SporOkulu,Basarilarimiz
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    keyword = request.GET.get("keyword")

    if keyword :
        anasayfa_haber = Haber.objects.all()

        liste3 = list()
        liste4 = list()
        
        for haber in anasayfa_haber:
            liste3.append(haber.haber_image)
            liste4.append(haber.id)

        a = liste3[-1]
        a1 = liste4[-1]
        b = liste3[-2]
        b1 = liste4[-2]
        
        anasayfa_duyuru = Duyuru.objects.filter(duyuru_title__contains = keyword)

        context_t = {
            "anasayfa_duyuru":anasayfa_duyuru,
            
            "a":a,
            "b":b,
            "a1":a1,
            "b1":b1,
        }
        
        return render(request,"index.html",context_t)
    
    
    anasayfa_haber = Haber.objects.all()
    anasayfa_duyuru = Duyuru.objects.all()

    liste = list()
    liste1 = list()
    
    for haber in anasayfa_haber:
        liste.append(haber.haber_image)
        liste1.append(haber.id)

    a = liste[-1]
    a1 = liste1[-1]
    b = liste[-2]
    b1 = liste1[-2]
    
    context = {
        "anasayfa_duyuru":anasayfa_duyuru,
        
        "a":a,
        "b":b,
        "a1":a1,
        "b1":b1,
    }
    return render(request,"index.html",context)


def news(request):
    anasayfa_haber = Haber.objects.all()
    context = {
        "anasayfa_haber": anasayfa_haber
    }
    return render(request,"haber.html",context)

def about(request):
    hakkimizda = Hakkimizda.objects.all()
    context = {
        "hakkimizda": hakkimizda
    }
    return render(request,"about.html",context)

def clubdetails(request):
    club = Club_information.objects.all()
    context = {
        "club": club
    }
    return render(request,"clubdetails.html",context)

@login_required(login_url = "user:login")
def EditPlayer(request):
    databases = Database.objects.filter(author = request.user)
    context = {
        "databases" : databases
    }
    
    return render(request,"editplayer.html",context)

@login_required(login_url = "user:login")
def AddPlayer(request):
    form = AddPlayerForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        database = form.save(commit=False)
        database.author = request.user
        database.save()

        messages.success(request,"Oyuncu Başarıyla Eklendi...")
        return redirect("database:addplayer")

    return render (request,"addplayer.html",{"form":form})


@login_required(login_url = "user:login")
def UpdatePlayer(request,id):
    player = get_object_or_404(Database,id = id)
    
    form = AddPlayerForm(request.POST or None,request.FILES or None,instance=player)

    if form.is_valid():
        player = form.save(commit=False)
        player.author = request.user
        player.save()
        messages.success(request,"Oyuncu Başarıyla Güncellendi...")
        return redirect("database:editplayer")
    return render(request,"updateplayer.html",{"form":form})

@login_required(login_url = "user:login")
def DeletePlayer(request,id):
    player = get_object_or_404(Database,id = id)
    player.delete()

    messages.success(request,"Oyuncu Başarıyla Silindi...")

    return redirect("database:editplayer")


@login_required(login_url = "user:login")
def EditGaleri(request):
    galeris = Galeri.objects.filter(author = request.user)
    context = {
        "galeris" : galeris
    }
    
    return render(request,"editgaleri.html",context)


@login_required(login_url = "user:login")
def AddGaleri(request):
    form = AddGaleriForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        galeri = form.save(commit=False)
        galeri.author = request.user
        galeri.save()

        messages.success(request,"Görsel Başarıyla Eklendi...")
        return redirect("database:editgaleri")

    return render (request,"addgaleri.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateGaleri(request,id):
    galeri = get_object_or_404(Galeri,id = id)
    
    form = AddGaleriForm(request.POST or None,request.FILES or None,instance=galeri)

    if form.is_valid():
        galeri = form.save(commit=False)
        galeri.author = request.user
        galeri.save()
        messages.success(request,"Görsel Başarıyla Güncellendi...")
        return redirect("database:editgaleri")
    return render(request,"updategaleri.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteGaleri(request,id):
    galeri = get_object_or_404(Galeri,id = id)
    galeri.delete()

    messages.success(request,"Görsel Başarıyla Silindi...")

    return redirect("database:editgaleri")


@login_required(login_url = "user:login")
def EditDuyuru(request):
    duyurular = Duyuru.objects.filter(author = request.user)
    context = {
        "duyurular" : duyurular
    }
    
    return render(request,"editduyuru.html",context)

@login_required(login_url = "user:login")
def AddDuyuru(request):
    form = AddDuyuruForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        duyuru = form.save(commit=False)
        duyuru.author = request.user
        duyuru.save()

        messages.success(request,"Duyuru Başarıyla Eklendi...")
        return redirect("database:editduyuru")

    return render (request,"addduyuru.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateDuyuru(request,id):
    duyuru = get_object_or_404(Duyuru,id = id)
    
    form = AddDuyuruForm(request.POST or None,request.FILES or None,instance=duyuru)

    if form.is_valid():
        duyuru = form.save(commit=False)
        duyuru.author = request.user
        duyuru.save()
        messages.success(request,"Duyuru Başarıyla Güncellendi...")
        return redirect("database:editduyuru")
    return render(request,"updateduyuru.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteDuyuru(request,id):
    duyuru = get_object_or_404(Duyuru,id = id)
    duyuru.delete()

    messages.success(request,"Duyuru Başarıyla Silindi...")

    return redirect("database:editduyuru")


@login_required(login_url = "user:login")
def EditHaber(request):
    haberler = Haber.objects.filter(author = request.user)
    context = {
        "haberler" : haberler
    }
    
    return render(request,"edithaber.html",context)

@login_required(login_url = "user:login")
def AddHaber(request):
    form = AddHaberForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        haber = form.save(commit=False)
        haber.author = request.user
        haber.save()

        messages.success(request,"Haber Başarıyla Eklendi...")
        return redirect("database:edithaber")

    return render (request,"addhaber.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateHaber(request,id):
    haber = get_object_or_404(Haber,id = id)
    
    form = AddHaberForm(request.POST or None,request.FILES or None,instance=haber)

    if form.is_valid():
        haber = form.save(commit=False)
        haber.author = request.user
        haber.save()
        messages.success(request,"Haber Başarıyla Güncellendi...")
        return redirect("database:edithaber")
    return render(request,"updatehaber.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteHaber(request,id):
    haber = get_object_or_404(Haber,id = id)
    haber.delete()

    messages.success(request,"Haber Başarıyla Silindi...")

    return redirect("database:edithaber")




def Team(request,id):
    if id == 1:
        
        oyuncular = Database.objects.filter(category = "A TAKIM")

        context = {
            
            "oyuncular" : oyuncular
        }

    if id == 2:
        
        oyuncular = Database.objects.filter(category = "A GENÇ")

        context = {
            
            "oyuncular" : oyuncular
        }

    if id == 3:
        oyuncular = Database.objects.filter(category = "U 19")

        context = {
            "oyuncular" : oyuncular
        }

    if id == 4:
        oyuncular = Database.objects.filter(category = "U 16")

        context = {
            "oyuncular" : oyuncular
        }

    if id == 5:
        oyuncular = Database.objects.filter(category = "U 15")

        context = {
            "oyuncular" : oyuncular
        }

    if id == 6:
        oyuncular = Database.objects.filter(category = "U 14")

        context = {
            "oyuncular" : oyuncular
        }

    if id == 7:
        oyuncular = Database.objects.filter(category = "U 13")

        context = {
            "oyuncular" : oyuncular
        }

    
        
    return render(request,"team.html",context)


def Spor_Okulu(request):
    sporokulu = SporOkulu.objects.all()
    context={
        "sporokulu":sporokulu
    }
    return render(request,"sporokulu.html",context)
    

def Basarılarımız(request):
    basarilarimiz = Basarilarimiz.objects.all()
    context={
        "basarilarimiz":basarilarimiz
    }
    return render(request,"basarılarımız.html",context)
    
def Oyuncularımız(request):

    keyword = request.GET.get("keyword")

    if keyword :
        oyuncular = Database.objects.filter(name__contains = keyword)
        
        return render(request,"oyuncularımız.html",{"oyuncular":oyuncular})

    oyuncular = Database.objects.all()
    context = {
        "oyuncular":oyuncular
    }
    return render(request,"oyuncularımız.html",context)

def Galerii(request):
    galeris = Galeri.objects.all()
    context={
        "galeris":galeris
    }
    return render(request,"galeri.html",context)

def Detail(request,id):
    oyuncu = get_object_or_404(Database,id = id)
    context = {
        "oyuncu":oyuncu
    }
    return render(request,"detail.html",context)

def HaberDetail(request,id):
    haber = get_object_or_404(Haber,id = id)
    context = {
        "haber":haber
    }
    return render(request,"haberdetail.html",context)

def PuanDurumu(request):
    return render(request,"puandurumu.html")
    

@login_required(login_url = "user:login")
def EditClub(request):
    clubs = Club_information.objects.filter(author = request.user)
    context = {
        "clubs" : clubs
    }
    
    return render(request,"editclub.html",context)

@login_required(login_url = "user:login")
def AddClub(request):
    form = AddClub_informationForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        club = form.save(commit=False)
        club.author = request.user
        club.save()

        messages.success(request,"Bilgi Başarıyla Eklendi...")
        return redirect("database:editclub")

    return render (request,"addclub.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateClub(request,id):
    club = get_object_or_404(Club_information,id = id)
    
    form = AddClub_informationForm(request.POST or None,request.FILES or None,instance=club)

    if form.is_valid():
        club = form.save(commit=False)
        club.author = request.user
        club.save()
        messages.success(request,"Bilgiler Başarıyla Güncellendi...")
        return redirect("database:editclub")
    return render(request,"updateclub.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteClub(request,id):
    club = get_object_or_404(Club_information,id = id)
    club.delete()

    messages.success(request,"Bilgiler Başarıyla Silindi...")

    return redirect("database:editclub")


@login_required(login_url = "user:login")
def EditHakkimizda(request):
    hakkimizda = Hakkimizda.objects.filter(author = request.user)
    context = {
        "hakkimizda" : hakkimizda
    }
    
    return render(request,"edithakkimizda.html",context)

@login_required(login_url = "user:login")
def AddHakkimizda(request):
    form = AddHakkimizdaForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        hakkimizda = form.save(commit=False)
        hakkimizda.author = request.user
        hakkimizda.save()

        messages.success(request,"Hakkımızda Başarıyla Eklendi...")
        return redirect("database:edithakkimizda")

    return render (request,"addhakkimizda.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateHakkimizda(request,id):
    hakkimizda = get_object_or_404(Hakkimizda,id = id)
    
    form = AddHakkimizdaForm(request.POST or None,request.FILES or None,instance=hakkimizda)

    if form.is_valid():
        hakkimizda = form.save(commit=False)
        hakkimizda.author = request.user
        hakkimizda.save()
        messages.success(request,"Hakkımızda Başarıyla Güncellendi...")
        return redirect("database:edithakkimizda")
    return render(request,"updatehakkimizda.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteHakkimizda(request,id):
    hakkimizda = get_object_or_404(Hakkimizda,id = id)
    hakkimizda.delete()

    messages.success(request,"Hakkımızda Başarıyla Silindi...")

    return redirect("database:edithakkimizda")

@login_required(login_url = "user:login")
def EditSporOkulu(request):
    sporokulu = SporOkulu.objects.filter(author = request.user)
    context = {
        "sporokulu" : sporokulu
    }
    
    return render(request,"editsporokulu.html",context)

@login_required(login_url = "user:login")
def AddSporOkulu(request):
    form = AddSporOkuluForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        sporokulu = form.save(commit=False)
        sporokulu.author = request.user
        sporokulu.save()

        messages.success(request,"SporOkulu Başarıyla Eklendi...")
        return redirect("database:editsporokulu")

    return render (request,"addsporokulu.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateSporOkulu(request,id):
    sporokulu = get_object_or_404(SporOkulu,id = id)
    
    form = AddSporOkuluForm(request.POST or None,request.FILES or None,instance=sporokulu)

    if form.is_valid():
        sporokulu = form.save(commit=False)
        sporokulu.author = request.user
        sporokulu.save()
        messages.success(request,"SporOkulu Başarıyla Güncellendi...")
        return redirect("database:editsporokulu")
    return render(request,"updatesporokulu.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteSporOkulu(request,id):
    sporokulu = get_object_or_404(SporOkulu,id = id)
    sporokulu.delete()

    messages.success(request,"SporOkulu Başarıyla Silindi...")

    return redirect("database:editsporokulu")

@login_required(login_url = "user:login")
def EditBasarilarimiz(request):
    basarilarimiz = Basarilarimiz.objects.filter(author = request.user)
    context = {
        "basarilarimiz" : basarilarimiz
    }
    
    return render(request,"editbasarilarimiz.html",context)

@login_required(login_url = "user:login")
def AddBasarilarimiz(request):
    form = AddBasarilarimizForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        basarilarimiz = form.save(commit=False)
        basarilarimiz.author = request.user
        basarilarimiz.save()

        messages.success(request,"Basarilarimiz Başarıyla Eklendi...")
        return redirect("database:editbasarilarimiz")

    return render (request,"addbasarilarimiz.html",{"form":form})

@login_required(login_url = "user:login")
def UpdateBasarilarimiz(request,id):
    basarilarimiz = get_object_or_404(Basarilarimiz,id = id)
    
    form = AddBasarilarimizForm(request.POST or None,request.FILES or None,instance=basarilarimiz)

    if form.is_valid():
        basarilarimiz = form.save(commit=False)
        basarilarimiz.author = request.user
        basarilarimiz.save()
        messages.success(request,"Basarilarimiz Başarıyla Güncellendi...")
        return redirect("database:editbasarilarimiz")
    return render(request,"updatebasarilarimiz.html",{"form":form})

@login_required(login_url = "user:login")
def DeleteBasarilarimiz(request,id):
    basarilarimiz = get_object_or_404(Basarilarimiz,id = id)
    basarilarimiz.delete()

    messages.success(request,"Basarilarimiz Başarıyla Silindi...")

    return redirect("database:editbasarilarimiz")

