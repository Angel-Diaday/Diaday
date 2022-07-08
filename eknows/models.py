from django.db import models

class ReportingParty(models.Model):
	rparty=models.CharField(max_length=30)
	raddress=models.TextField()
	rcontact=models.IntegerField(max_length=11)

class VictimsInformation(models.Model):
	rpartyId=models.ForeignKey(ReportingParty, default=None, on_delete=models.CASCADE)
	vtype = models.CharField (max_length=30)
	vdate = models.TextField(max_length=10, default="")
	vtime = models.TextField(max_length=5)
	vname = models.CharField (max_length=30)
	vaddress = models.TextField()
	vcontact = models.IntegerField(max_length=11)
	vdescription = models.TextField()

class NGO(models.Model):
	ngdonator = models.CharField(max_length=20)
	ngaddress = models.CharField(max_length=40)
	ngcontact = models.IntegerField(max_length=11)
	ngname = models.CharField(max_length=40)
	ngplace = models.CharField(max_length=40)
	ngdonation = models.TextField()

class Summary(models.Model):
	reportparty = models.ForeignKey(ReportingParty, default=None, on_delete=models.CASCADE)
	victims = models.ForeignKey(VictimsInformation, default=None, on_delete=models.CASCADE)

