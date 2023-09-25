from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.trangchu, name="trangchu"),
    path('timkiem/', views.timkiem, name="timkiem"),
    path('blog/', views.blog  , name="blog"),
    path('lienhe/', views.lienhe  , name="lienhe"),
    path('updateItem/', views.updateItem  , name="updateItem"),

    path('giohang/', views.giohang  , name="giohang"),
    path('muahang/', views.muahang  , name="muahang"),
    path('hoadon/', views.hoadon  , name="hoadon"),
     path('donhangcuatoi/', views.donhangcuatoi  , name="donhangcuatoi"),

    
    path('dangnhap/', views.dangnhap  , name="dangnhap"),
    path('dangxuat/', views.dangxuat, name="dangxuat"),
    path('dangky/', views.dangky  , name="dangky"),
    
    path('baomat/', views.baomat  , name="baomat"),
    

    path('thongtincanhan/', views.thongtincanhan , name="thongtincanhan" ),
    path('suathongtincanhan/', views.suathongtincanhan , name="suathongtincanhan" ),
    path('themdiachi/', views.themdiachi , name="themdiachi" ),
    path('suadiachi/', views.suadiachi , name="suadiachi" ),
    path('xoadiachi/', views.xoadiachi , name="xoadiachi" ),

    path('chitiet/', views.chitiet , name="chitiet" ),

    path('hang/', views.hang , name="hang" ),

    # phan admin
    path('manage/', views.manage , name="manage" ),

    path('quanlyhang/', views.quanlyhang , name="quanlyhang" ),
    path('themhang/', views.themhang , name="themhang" ),
    path('suahang/', views.suahang , name="suahang" ),
    path('xoahang/', views.xoahang , name="xoahang" ),

    path('quanlysanpham/', views.quanlysanpham , name="quanlysanpham" ),
    path('themsanpham/', views.themsanpham , name="themsanpham" ),
    path('xemsanpham/', views.xemsanpham , name="xemsanpham" ),
    path('suasanpham/', views.suasanpham , name="suasanpham" ),
    path('xoasanpham/', views.xoasanpham , name="xoasanpham" ),

    path('quanlythanhvien/', views.quanlythanhvien , name="quanlythanhvien" ),
    path('themthanhvien/', views.themthanhvien , name="themthanhvien" ),
    path('xemthanhvien/', views.xemthanhvien , name="xemthanhvien" ),
    path('xoathanhvien/', views.xoathanhvien , name="xoathanhvien" ),

    path('quanlydonhang/', views.quanlydonhang , name="quanlydonhang" ),
    path('xemdonhang/', views.xemdonhang , name="xemdonhang" ),
    path('xoadonhang/', views.xoadonhang , name="xoadonhang" ),
    #API

]



