# from itertools import product
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
# app
from .python.app.base import *
from .python.app.updateItem import updateItem
from .python.app.timkiem import timkiem
from .python.app.lienhe import lienhe
from .python.app.baomat import baomat

from .python.app.giohang import giohang
from .python.app.muahang import muahang
from .python.app.hoadon import hoadon
from .python.app.donhangcuatoi import donhangcuatoi

from .python.app.dangky import dangky
from .python.app.dangnhap import dangnhap,dangxuat
from .python.app.blog import blog
from .python.app.thongtincanhan import thongtincanhan,suathongtincanhan
from .python.app.diachi import themdiachi,suadiachi,xoadiachi
from .python.app.chitiet import chitiet



from .python.app.hang import hang
# admin
from .python.admin.manage import manage

from .python.admin.quanlyhang import quanlyhang,themhang,suahang,xoahang

from .python.admin.quanlysanpham import quanlysanpham,themsanpham,xemsanpham,suasanpham,xoasanpham

from .python.admin.quanlythanhvien import quanlythanhvien,themthanhvien,xemthanhvien,xoathanhvien

from .python.admin.quanlydonhang import quanlydonhang,xemdonhang,xoadonhang


#API






