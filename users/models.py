from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    # image = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_added = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        get_latest_by = ['date_added']
