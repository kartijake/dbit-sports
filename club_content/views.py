from django.shortcuts import render
from .models import images_for_club
# Create your views here.
def content(request):
	img=images_for_club.objects.get(id=2)
	dic={'obj':img}
	return render(request,'event_gallery.html',dic)
