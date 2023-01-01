from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    colors = [
        ("bg-danger","Red"),
        ("bg-info","Teal"),
        ("bg-success","Green"),
        ("bg-warning","Yellow"),
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=10,choices=colors,default="Teal")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
        