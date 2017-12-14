from django.db import models


class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_date = models.DateField
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


