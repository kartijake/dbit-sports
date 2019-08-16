from django.db import models

# Create your models here.
class images_for_club(models.Model):
	image_field=models.ImageField(upload_to='image')