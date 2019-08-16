from django.shortcuts import render
from .models import UpcomingEvents, RecentEvents
from datetime import date


# Create your views here.


def home(request):
    try:
        UpEvents = list(UpcomingEvents.objects.all())
        RecEvents = list(RecentEvents.objects.all())
        up = UpcomingEvents()
        events_dic = {
            "upcoming": UpEvents,
            "recent": RecEvents
        }
        for event in UpEvents:
            if event.date == date.today():
                UpcomingEvents.objects.get(date=date.today()).delete()
                recent = RecentEvents.objects.create(
                    name=event.name, date=event.date)
                up.save()
                recent.save()
                print(date.today() == event.date)
    except:
        print("Error")

    return render(request, 'home.html', context=events_dic)


def about(request):
    return render(request, 'About.html', {})


def college_event(request):
    return render(request, 'college_evnets.html', {})


def vtu_event(request):
    return render(request, 'vtu-event.html', {})


def nss(request):
    return render(request, 'nss.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def alumini(request):
    return render(request, 'alumini.html', {})


def awards(request):
    return render(request, 'awards.html', {})


def teamlist(request):
    return render(request, 'teamlist.html', {})

def ped(request):
    return render(request, 'PED.html', {})


# def sports(request, category):
# 	sports = Sports.objects.get(name=cat)
#     image = Image.objects.filter(name=cat)
#     my_dic = {
#         'sports': sports,
#         'images': list(image)
#     	}
# 	return render(request,'categories.html',context=my_dic)
