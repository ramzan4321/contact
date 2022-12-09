from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.name+" "+str(self.email)