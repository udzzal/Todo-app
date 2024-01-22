from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo_task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    titel=models.CharField(max_length=250)
    created_date=models.DateTimeField(auto_now=True)
    description=models.TextField()
    complete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.titel
    
    class Meta:
        ordering=['complete']
        
        