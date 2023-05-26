from django.db import models

# Create your models here.
from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
