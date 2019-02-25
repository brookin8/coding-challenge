from django.db import models

class Referral(models.Model):
    title = models.CharField(max_length=255, null=False)
    clicks = models.IntegerField(default = 0)

    def __str__(self):
        return "{} - {}".format(self.title, self.clicks)