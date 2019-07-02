from django.db import models

# Create your models here.

class Todolist(models.Model):
    PRIORITY_CHOICES =\
    (
        ('2', 'High'),
        ('1', 'Low'),
    )

    COMPLPETE_CHOICES =\
    (
        ('0', 'Pending'),
        ('1', 'Complete'),
    )

    id = models.AutoField(primary_key=True) # for object referencing
    name = models.CharField(max_length=50) # name of the item
    content = models.TextField() # description of the item
    expire_date = models.DateField() # when the item is expire
    status = models.CharField(max_length=1, choices=COMPLPETE_CHOICES, default='0') # the complete status of the item
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1') # the priority of the item

    def __str__(self):
        return f'{self.name} ({self.id})'
