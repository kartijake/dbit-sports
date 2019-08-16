from django.db import models

# Create your models here.
class men_100_meter(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_200_meter(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_400_meter(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_800_meter(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_1500_meter(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_shot_put(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_discus(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_javelin(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_Long_jump(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)

class men_relay(models.Model):
	place=models.IntegerField()
	student_name=models.CharField(max_length=20)
	semister=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)