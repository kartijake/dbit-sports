"""college_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import home as homepage, about, college_event, vtu_event, nss, gallery, alumini, awards, teamlist,ped,ex
from event_list.views import event_results
from club_content.views import content
from home.views import category
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('About/', about, name='About'),
    path('vtu_events/', vtu_event, name='vtu_events'),
    path('NSS/', nss, name='NSS'),
    path('Gallery/', gallery, name='gallery'),
    path('college_event/', college_event, name='college_event'),
    path('college_results/', event_results, name='college_results'),
    path('templets/event_gallery.html', content, name='content'),
    path('alumini/', alumini, name='alumini'),
    path('awards/', awards, name='awards'),
    path('category=<cat>/', category),
    path('administrative', teamlist, name="administrative"),
     path('administrative/ped', ped, name="administrative/ped"),
        path('ex', ex, name="ex"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
