from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ReportingParty,VictimsInformation



def MainPage(request):
   return render(request, 'index.html')

def rescueForm(request):

   if request.method == "POST":
      reportparty = ReportingParty.objects.create(rparty=request.POST['rparty'],
         raddress=request.POST['raddress'],
         rcontact=request.POST['rcontact'],)

      reportparty.save()

      return redirect(f'/index2/{reportparty.id}')
   else:
      return render(request, 'index1.html')

def index2(request, reportpartyID):
   report = ReportingParty.objects.get(id=reportpartyID)
   if request.method == "POST":
      victims = VictimsInformation.objects.create(rpartyId=report,
         vtype=request.POST['rescuetype'],
         vdate=request.POST['vdate'],
         vtime=request.POST['vtime'],
         vname=request.POST['vname'],
         vaddress=request.POST['vaddress'],
         vcontact=request.POST['vcontact'],
         vdescription=request.POST['vdescription'],)
      victims.save()

      return redirect(f'/summary/{report.id}')
   else:
      return render(request, 'index2.html')

def summary(request, reportID):
   report = ReportingParty.objects.get(id=reportID)
   victim = VictimsInformation.objects.all()

   return render(request, 'Summary.html', {'victims':victim, 'reports':report})

def delete(request,reportID, itemID):
   report=ReportingParty.objects.get(id=reportID)
   item = VictimsInformation.objects.get(id=itemID)
   item.delete()
   return redirect(f'/summary/{report.id}')
   # return redirect(f'/summary/{report}')


def earthQuakes(request):
   return render(request, 'Definition.html')

def Definition(request):
   return render(request, 'Definition.html')
def EarthquakeTypes(request):
   return render(request, 'Earthquaketypes.html')
def PBoundaries(request):
   return render(request, 'Plateboundaries.html')
def Measurement(request):
   return render(request, 'Measurements.html')
def FocusEpicenter(request):
   return render(request, 'FocusandEpicenter.html')
def Faultline(request):
   return render(request, 'FaultLine.html')
def SurfaceFaulting(request):
   return render(request, 'Surfacefaulting.html')
def GroundShaking(request):
   return render(request, 'Groundshaking.html')
def Landslide(request):
   return render(request, 'Landslide.html')
def TectonicDeform(request):
   return render(request, 'Tectonicdeformation.html')
def Tsunami(request):
   return render(request, 'Tsunami.html')

def Trivias(request):
   return render(request, 'History.html')

def SixFacts(request):
   return render(request, 'Sixfacts.html')

def TenPowerful(request):
   return render(request, 'Tenpowerful.html')
def Sumatra(request):
   return render(request, 'Sumatra.html')
def AssamTibet(request):
   return render(request, 'AssamTibet.html')
def RatIslands(request):
   return render(request, 'RatIslands.html')
def Ecuadorcolombia(request):
   return render(request, 'EcuadorColombia.html')
def Maule(request):
   return render(request, 'Maule.html')
def Kamchatka(request):
   return render(request, 'Kamchatka.html')
def Tohoku(request):
   return render(request, 'Tohoku.html')
def Sumatra2(request):
   return render(request, 'Sumatra_2.html')
def GreatAlaska(request):
   return render(request, 'GreatAlaska.html')
def Valdivia(request):
   return render(request, 'Valdivia.html')

def TenDeadliest(request):
   return render(request, 'Tendeadliest.html')
def Shaanxi(request):
   return render(request, 'Shaanxi.html')
def Tangshan(request):
   return render(request, 'Tangshan.html')
def IndianOcean(request):
   return render(request, 'IndianOcean.html')
def Haiyuan(request):
   return render(request, 'Haiyuan.html')
def Kanto(request):
   return render(request, 'Kanto.html')
def Turkmenistan(request):
   return render(request, 'Turkmenistan.html')
def Sichuan(request):
   return render(request, 'Sichuan.html')
def Kashmir(request):
   return render(request, 'Kashmir.html')
def Messina(request):
   return render(request, 'Messina.html')
def Chimbote(request):
   return render(request, 'Chimbote.html')

def HistoryEarthquake(request):
   return render(request, 'Historyofearthquake.html')
def LuzonEarthquake(request):
   return render(request, 'LuzonEarthquake.html')
def Casiguran(request):
   return render(request, 'Casiguran.html')
def MoroGulf(request):
   return render(request, 'MoroGulf.html')
def Bohol(request):
   return render(request, 'Bohol.html')
def Laoag(request):
   return render(request, 'Laoag.html')
def Negros(request):
   return render(request, 'Negros.html')

def TenStrongest(request):
   return render(request, 'Tenstrongest.html')
def Mindanao8(request):
   return render(request, 'Mindanao8.html')
def CLuzon78(request):
   return render(request, 'CLuzon7.8.html')
def Luzon75(request):
   return render(request, 'Luzon7.5.html')
def Casiguran73(request):
   return render(request, 'Casiguran7.3.html')
def Bohol72(request):
   return render(request, 'Bohol7.2.html')
def Mindoro71(request):
   return render(request, 'Mindoro7.1.html')
def CVisayas(request):
   return render(request, 'CVisayas.html')
def SMindanao(request):
   return render(request, 'SMindanao7.5.html')
def NIlocos(request):
   return render(request, 'Ilocos.html')
def ESamar(request):
   return render(request, 'ESamar7.6.html')

def EightCities(request):
   return render(request, 'Eightcities.html')

def Contact(request):
   return render(request, 'Contact.html')
def Before(request):
   return render(request, 'Before.html')
def During(request):
   return render(request, 'During.html')
def After(request):
   return render(request, 'After.html')
def EKit(request):
   return render(request, 'EKit.html')
def AidKits(request):
   return render(request, 'Kit.html')
def NDRRMC(request):
   return render(request, 'NDRRMC.html')
def PAGASA(request):
   return render(request, 'PAGASA.html')
def PHIVOLCS(request):
   return render(request, 'PHIVOLCS.html')
def DENR(request):
   return render(request, 'DENR.html')
def DOST(request):
   return render(request, 'DOST.html')
def AFP(request):
   return render(request, 'AFP.html')

def AboutUs(request):
   return render(request, 'About.html')





# def MainPage(request):
#    if request.method == "POST":
#       rparty = request.POST ['rparty']
#       raddress = request.POST ['raddress']
#       rcontact = request.POST ['rcontact']

#       return redirect(f'/eknows/create/{ReportingParty}')
#    else:
#       return render(request, 'mainpage.html')

# def index2(request):
#    return render(request, 'index2.html')

# def index3(request):
#    if request.method == "POST":
#       lgname = request.POST ['lgname']
#       lgaddress = request.POST ['lgaddress']
#       lgcontact = request.POST ['lgcontact']
#       lgplace = request.POST ['lgplace']
#       lgdescription = request.POST ['lgdescription']

#       lgsum = LGUSum(lgname= lgname, lgaddress= lgaddress, lgcontact= lgcontact, 
#          lgplace = lgplace, lgdescription=lgdescription)
#       lgsum.save()

#    else:
#       return render(request, 'index3.html')
#    lgsummary = LGUSum.objects.all()
#    return render(request, 'index3.html', {'lgsummary':lgsummary})

#    if request.method == "POST":
#       ngdonator = request.POST ['ngdonator']
#       ngaddress = request.POST ['ngaddress']
#       ngcontact = request.POST ['ngcontact']
#       ngname = request.POST ['ngname']
#       ngplace = request.POST ['ngplace']
#       ngdescription = request.POST ['ngdescription']

#       ngsum = NGOSum( ngdonator= ngdonator, ngaddress= ngaddress, ngcontact= ngcontact, ngname= ngname,
#          ngplace = ngplace, ngdescription=ngdescription)
#       ngsum.save()

#    else:
#       return render(request, 'index3.html')
#    ngsummary = NGOSum.objects.all()
#    return render(request, 'index3.html', {'ngsummary':ngsummary})

# def MainPage(request):     
#    return render(request, 'Rescue Form.html')