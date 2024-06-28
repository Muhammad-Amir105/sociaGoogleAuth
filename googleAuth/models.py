from django.db import models


# Create your models here.
class UserProfile(models.Model):
    google_user_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)

    # Add any additional fields as needed

    def __str__(self):
        return self.email
