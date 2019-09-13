from django.db import models

# Create your models here.


class Sports(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.ForeignKey(Sports, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    player_name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return str(self.name)+" "+str(self.player_name)


class Clubs(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Club_image(models.Model):
    name = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/clubs/')


class Facilities(models.Model):
    name = models.ForeignKey(Sports, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)+" "+str(self.img_name)
