from django.db import models

class BaseModel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.title