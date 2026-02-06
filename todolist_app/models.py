from django.db import models
from  datetime import date
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    date=models.DateField(default=date.today)
    status=None
    def __str__(self):
        if self.done==True:
            self.status="Completed"
        else:
             self.status="Not COmpleted"
        return f"{self.task} created on {self.date} Task-{self.status}"
