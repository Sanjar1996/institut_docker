from django.shortcuts import render, redirect

from .models import *


def index(request):
    carusel = HomeCarusel.objects.all()
    news = HomeNews.objects.all()
    video = HomeVideo.objects.all()
    qonun = Qaror.objects.all()
    context = {
        'carusel': carusel,
        'news': news,
        'video': video,
        'qonun': qonun,
    }
    return render(request, 'index.html', context)


def price(request):
    pricemodel = ByudjetModel.objects.all()
    priceplan = ByudjetPlan.objects.all()
    context = {
        'pricemodel': pricemodel,
        'priceplan': priceplan,
    }
    return render(request, 'pricing.html', context)


def xodim(request):
    employe = Xodim.objects.all()
    context = {
        'xodim': employe,
    }
    return render(request, 'team.html', context)


def about(request):
    emplope = Xodim.objects.all()
    context = {
        'employe': emplope
    }
    return render(request, 'about.html', context)


def document(request):
    dock = DockModel.objects.all()
    return render(request, 'dockument.html', {'dock': dock})


def qaror(request):
    qaror = Qaror.objects.all()
    return render(request, 'qaror.html', {'qaror': qaror})


def tuzilma(request):
    return render(request, 'tuzilma.html')


def farmon(request):
    farmon = Farmon.objects.all()
    return render(request, 'farmon.html', {'farmon': farmon})


def service(request):
    servis = Service.objects.all()
    return render(request, 'services.html', {'servis': servis})


def price_plan(request, pk):
    pricemodel = ByudjetModel.objects.get(id=pk)
    plans = ByudjetPlan.objects.filter(titleTwo_id=pk)
    context = {
        'plans': plans,
        'pricemodel': pricemodel,
    }
    return render(request, 'price_plan.html', context)


def contact(request):
    if request.method == 'POST':
        aloqa = Contact(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                        message=request.POST['message'])
        aloqa.save()
        return redirect('home')
    return render(request, 'contact.html')


def yangilik(request):
    db_news = YangilikModel.objects.all()
    context = {
        'baza': db_news,
    }
    return render(request, 'yangiliklar.html', context)


def detailview(request, pk):
    news = YangilikModel.objects.get(id=pk)
    context = {
        'news': news
    }
    return render(request, 'detail.html', context)
