from django.db import models

# Create your models here.

class registr(models.Model):
	username=models.CharField(max_length=100)
	address=models.CharField(max_length=20)
	age=models.CharField(max_length=10)
	mobile=models.CharField(max_length=10)
	dob=models.EmailField()
	activate = models.BooleanField(default=0)

class candidate(models.Model):
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	party=models.CharField(max_length=100)
	state=models.CharField(max_length=100)


class admregister(models.Model):
	name=models.CharField(max_length=100)
	password=models.CharField(max_length=20)
	email=models.EmailField()

