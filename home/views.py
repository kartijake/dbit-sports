from django.shortcuts import render
from django.http import HttpResponse
from home.models import Image, Sports, Facilities, Club_image, Clubs
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
    print(image.image)
    return render(request, "categories.html", context=my_dic)


def club(request, club=None):
    club_name = Clubs.objects.get(name=club)
    image = Club_image.objects.filter(name=club)

    my_dic = {
        'club_name': str(club_name).capitalize(),
        'club_data': club_name.data,
        'image': image
    }
    print(club_name.data)
    return render(request, 'event_gallery.html', context=my_dic)
