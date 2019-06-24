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

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    expire_date = models.DateField()
    status = models.CharField(max_length=1, choices=COMPLPETE_CHOICES, default='0')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1')

    def __str__(self):
        return f'{self.name} ({self.id})'
