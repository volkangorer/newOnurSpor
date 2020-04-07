from . import views

from django.contrib import admin
from django.urls import path,include


app_name = "database"


urlpatterns = [
    path('clubdetails/', views.clubdetails,name = "clubdetails"),
    path('news/', views.news,name = "news"),

    path('editplayer/', views.EditPlayer,name = "editplayer"),
    path('addplayer/', views.AddPlayer,name = "addplayer"),
    path('updateplayer/<int:id>', views.UpdatePlayer,name = "updateplayer"),
    path('deleteplayer/<int:id>', views.DeletePlayer,name = "deleteplayer"),
    
    path('editgaleri/', views.EditGaleri,name = "editgaleri"),
    path('addgaleri/', views.AddGaleri,name = "addgaleri"),
    path('updategaleri/<int:id>', views.UpdateGaleri,name = "updategaleri"),
    path('deletegaleri/<int:id>', views.DeleteGaleri,name = "deletegaleri"),
    
    path('editduyuru/', views.EditDuyuru,name = "editduyuru"),
    path('addduyuru/', views.AddDuyuru,name = "addduyuru"),
    path('updateduyuru/<int:id>', views.UpdateDuyuru,name = "updateduyuru"),
    path('deleteduyuru/<int:id>', views.DeleteDuyuru,name = "deleteduyuru"),

    path('edithaber/', views.EditHaber,name = "edithaber"),
    path('addhaber/', views.AddHaber,name = "addhaber"),
    path('updatehaber/<int:id>', views.UpdateHaber,name = "updatehaber"),
    path('deletehaber/<int:id>', views.DeleteHaber,name = "deletehaber"),

    path('editclub/', views.EditClub,name = "editclub"),
    path('addclub/', views.AddClub,name = "addclub"),
    path('updateclub/<int:id>', views.UpdateClub,name = "updateclub"),
    path('deleteclub/<int:id>', views.DeleteClub,name = "deleteclub"),

    path('edithakkimizda/', views.EditHakkimizda,name = "edithakkimizda"),
    path('addhakkimizda/', views.AddHakkimizda,name = "addhakkimizda"),
    path('updatehakkimizda/<int:id>', views.UpdateHakkimizda,name = "updatehakkimizda"),
    path('deletehakkimizda/<int:id>', views.DeleteHakkimizda,name = "deletehakkimizda"),

    path('editsporokulu/', views.EditSporOkulu,name = "editsporokulu"),
    path('addsporokulu/', views.AddSporOkulu,name = "addsporokulu"),
    path('updatesporokulu/<int:id>', views.UpdateSporOkulu,name = "updatesporokulu"),
    path('deletesporokulu/<int:id>', views.DeleteSporOkulu,name = "deletesporokulu"),

    path('editbasarilarimiz/', views.EditBasarilarimiz,name = "editbasarilarimiz"),
    path('addbasarilarimiz/', views.AddBasarilarimiz,name = "addbasarilarimiz"),
    path('updatebasarilarimiz/<int:id>', views.UpdateBasarilarimiz,name = "updatebasarilarimiz"),
    path('deletebasarilarimiz/<int:id>', views.DeleteBasarilarimiz,name = "deletebasarilarimiz"),



    
    

    path('team/<int:id>', views.Team,name = "team"),

    path('sporokulu/', views.Spor_Okulu,name = "sporokulu"),
    path('puandurumu/', views.PuanDurumu,name = "puandurumu"),
    path('basarılarımız/', views.Basarılarımız,name = "basarılarımız"),
    path('galeri', views.Galerii,name = "galeri"),
    path('oyuncularımız/', views.Oyuncularımız,name = "oyuncularımız"),
    path('detail/<int:id>', views.Detail,name = "detail"),
    path('haber_detail/<int:id>', views.HaberDetail,name = "haber_detail"),
    
]