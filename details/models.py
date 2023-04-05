from django.db import models


class Details(models.Model):
    details_type = models.CharField(max_length=255)
    details_model = models.CharField(max_length=255)
    details_name = models.TextField(blank=True)
    details_price = models.TextField(blank=True)
    deteils_description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        # sd = str(self.type) + (self.name) + f'Цена: {self.details_price}'
        return self.details_name
