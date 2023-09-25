from django.shortcuts import render


def manage(request):
    context ={}
    return render(request, 'admin/manage.html', context)
