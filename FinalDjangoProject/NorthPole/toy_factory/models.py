from django.db import models
from santa_list.models import Kid  # Import Kid model from santa_list app

class Toy(models.Model):
    kid = models.OneToOneField(Kid, on_delete=models.CASCADE)
    toy_type = models.CharField(max_length=255)  # The toy the child requested

    def __str__(self):
        return f"{self.kid.name} - {self.toy_type}"

class Coal(models.Model):
    kid = models.OneToOneField(Kid, on_delete=models.CASCADE)
    reason = models.TextField()  # Reason for coal (punishment)

    def __str__(self):
        return f"{self.kid.name} - Coal"
