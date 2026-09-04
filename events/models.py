from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_mail = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EventsModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)

    banner = models.ImageField(upload_to="images/", default="defaults/default_banner.webp")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100)
    host = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title