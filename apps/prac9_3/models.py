from django.db import models

# Create your models here.
class formSchema(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username
    
    class Meta:
        app_label = 'apps.prac9_3'
