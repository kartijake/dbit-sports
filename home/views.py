from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image, Sports, Facilities
# Create your views here.


def category(request, cat=None):

    sports = Sports.objects.get(name=cat)
    fac = list(Facilities.objects.filter(name=cat))
    img = list(Image.objects.filter(name=cat))
    my_dic = {
        'sports': sports,
        'facilities': fac,
        'achievers': img


    }
    print(sports)
    return render(request, "categories.html", context=my_dic)
