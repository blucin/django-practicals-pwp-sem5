from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class fileFormSchema(models.Model):
    fileName = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fileName