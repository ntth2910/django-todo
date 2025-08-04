from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # use __str__ to return a string representation of the model
    def __str__(self):
        return self.task