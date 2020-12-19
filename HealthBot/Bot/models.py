from django.db import models
from django.contrib.auth.models import User

# User Registration Model

'''class Profile(models.Model):
    user_name = models.OneToOneField(User,blank=False, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False)
    password = models.TextField(blank=False,null=False)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
'''

