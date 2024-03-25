from django.db import models

# Create your models here.
class doctor(models.Model):
 doctor_id=models.IntegerField(primary_key=True)
 name=models.CharField(max_length=15)
 age=models.IntegerField()
 experience=models.IntegerField()
 speciality=models.CharField(max_length=100)
 id=models.IntegerField()
 api_key=models.TextField()
 location=models.CharField(max_length=15)

class hospitals(models.Model):
  hospital_id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=30)
  location=models.CharField(max_length=25)
  ambulances=models.IntegerField()


class prescription(models.Model):
  pres_id=models.IntegerField(primary_key=True)
  patient_id=models.IntegerField()
  doctor_id=models.IntegerField()
  patient_name=models.CharField(max_length=15)
  medecine=models.CharField(max_length=15)
  reason=models.CharField(max_length=15)
  Time_medication=models.CharField(max_length=15)

class patients(models.Model):
   patient_id=models.IntegerField(primary_key=True)
   doctor_id=models.IntegerField()
   name=models.CharField(max_length=15)
   age=models.IntegerField()
   medical_history=models.CharField(max_length=15)
   allarges=models.CharField(max_length=15)
   health_status=models.BooleanField()
   mental_health=models.BooleanField()
class api_keys(models.Model):
  id=models.IntegerField(primary_key=True)
  uname=models.TextField()
  api_key=models.TextField()