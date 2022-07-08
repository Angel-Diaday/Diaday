from django.contrib import admin
from .models import *

admin.site.register([ReportingParty, VictimsInformation, NGO, Summary])
