from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import *


def base(request):
    
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    context = {
        'categories': categories,
        'show_manage': show_manage,
    }
    return render(request, 'app/base.html',context)



def trangchu(request):
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    products = Product.objects.all()
    paginator = Paginator(products, 8)  # Chia danh sách sản phẩm thành các trang, mỗi trang có 8 sản phẩm

    page_number = request.GET.get('page')  # Lấy số trang từ tham số truy vấn URL
    page = paginator.get_page(page_number)  # Lấy trang hiện tại
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            print(item)
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        items = []
        user_not_login = "show"
        user_login = "none"

    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    active_category = request.GET.get('category', '')
    context = {'products': products,
               'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'active_category': active_category,
               'show_manage': show_manage,
               'page': page,
               }
    return render(request, 'app/trangchu.html', context)


def show_manage(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    return show_manage