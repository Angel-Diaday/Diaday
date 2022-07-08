"""eqproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from eknows import views
from django.urls import re_path as url

urlpatterns = [ path('admin/', admin.site.urls), 
path('', views.MainPage, name='index'), 
path('index1/', views.rescueForm, name='index1'),
url(r'^index2/(\d+)/$', views.index2, name='index2'),
url(r'^summary/(\d+)/$', views.summary, name='summary'),
url(r'^delete/(\d+)/(\d+)/$', views.delete, name='delete'),


path('earthquakes/', views.earthQuakes, name='earthquakes/'), 
path('definition/', views.Definition, name='definition/'), 
path('earthquaketypes/', views.EarthquakeTypes, name='earthquaketypes/'), 
path('plateboundaries/', views.PBoundaries, name='plateboundaries/'), 
path('measurements/', views.Measurement, name='measurements/'), 
path('focusepicenter/', views.FocusEpicenter, name='focusepicenter/'),
path('faultline/', views.Faultline, name='faultline/'), 
path('surfacefaulting/', views.SurfaceFaulting, name='surfacefaulting/'), 
path('groundshaking/', views.GroundShaking, name='groundshaking/'), 
path('landslide/', views.Landslide, name='landslide/'), 
path('tectonicdeform/', views.TectonicDeform, name='tectonicdeform/'), 
path('tsunami/', views.Tsunami, name='tsunami/'),

path('trivias/', views.Trivias, name='trivias/'),
path('sixfacts/', views.SixFacts, name='sixfacts/'),
path('tenpowerful/', views.TenPowerful, name='tenpowerful/'),
path('sumatra/', views.Sumatra, name='sumatra/'),
path('assamtibet/', views.AssamTibet, name='assamtibet/'),
path('ratislands/', views.RatIslands, name='ratislands/'),
path('ecuadorcolombia/', views. Ecuadorcolombia, name='ecuadorcolombia/'),
path('maule/', views.Maule, name='maule/'),
path('kamchatka/', views.Kamchatka, name='kamchatka/'),
path('tohoku/', views.Tohoku, name='tohoku/'),
path('sumatra2/', views.Sumatra2, name='sumatra2/'),
path('greatalaska/', views.GreatAlaska, name='greatalaska/'),
path('valdivia/', views.Valdivia, name='valdivia/'),

path('tendeadliest/', views.TenDeadliest, name='tendeadliest/'),
path('shaanxi/', views.Shaanxi, name='shaanxi/'),
path('tangshan/', views.Tangshan, name='tangshan/'),
path('indianocean/', views. IndianOcean, name='indianocean/'),
path('haiyuan/', views.Haiyuan, name='haiyuan/'),
path('kanto/', views.Kanto, name='kanto/'),
path('turkmenistan/', views.Turkmenistan, name='turkmenistan/'),
path('sichuan/', views.Sichuan, name='sichuan/'),
path('kashmir/', views.Kashmir, name='kashmir/'),
path('messina/', views.Messina, name='messina/'),
path('chimbote/', views.Chimbote, name='chimbote/'),

path('historyearthquake/', views.HistoryEarthquake, name='historyearthquake/'),
path('luzonearthquake/', views.LuzonEarthquake, name='luzonearthquake/'),
path('casiguran/', views.Casiguran, name='casiguran/'),
path('morogulf/', views.MoroGulf, name='morogulf/'),
path('bohol/', views.Bohol, name='bohol/'),
path('laoag/', views.Laoag, name='laoag/'),
path('negros/', views.Negros, name='negros/'),

path('tenstrongest/', views.TenStrongest, name='tenstrongest/'),
path('mindanao8/', views.Mindanao8, name='mindanao8/'),
path('cluzon7.8/', views.CLuzon78, name='cluzon7.8/'),
path('luzon7.5/', views.Luzon75, name='luzon7.5/'),
path('casiguran7.3/', views.Casiguran73, name='casiguran7.3/'),
path('bohol7.2/', views.Bohol72, name='bohol7.2/'),
path('mindoro7.1/', views.Mindoro71, name='mindoro7.1/'),
path('cvisayas/', views.CVisayas, name='cvisayas/'),
path('smindanao7.5/', views.SMindanao, name='smindanao7.5/'),
path('ilocos/', views.NIlocos, name='ilocos/'),
path('esamar/', views.ESamar, name='esamar/'),

path('eightcities/', views.EightCities, name='eightcities/'),

path('contact/', views.Contact, name= 'contact/'),
path('before/', views.Before, name='before/'),
path('during/', views.During, name='during/'),
path('after/', views.After, name='after/'),
path('ekit/', views.EKit, name='ekit/'),
path('aidkit/', views.AidKits, name='aidkit/'),
path('ndrrmc/', views.NDRRMC, name='ndrrmc/'),
path('pagasa/', views.PAGASA, name='pagasa/'),
path('phivolcs/', views.PHIVOLCS, name='phivolcs/'),
path('denr/', views.DENR, name='denr/'),
path('dost/', views.DOST, name='dost/'),
path('afp/', views.AFP, name='afp/'),

path('aboutus/', views.AboutUs, name='aboutus/'),
]