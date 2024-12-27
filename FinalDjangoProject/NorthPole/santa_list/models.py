from django.db import models

class Kid(models.Model):
    name = models.CharField(max_length=100)
    niceness_coefficient = models.FloatField()  # Behavior coefficient
    gift = models.CharField(max_length=255, null=True, blank=True)  # Toy request

    def __str__(self):
        return self.name

class SantasList(models.Model):
    naughty_list = models.ManyToManyField(Kid, related_name='naughty_list', blank=True)
    nice_list = models.ManyToManyField(Kid, related_name='nice_list', blank=True)

    def generate_lists(self):
        for kid in Kid.objects.all():
            if kid.niceness_coefficient >= 0.5:
                self.nice_list.add(kid)
            else:
                self.naughty_list.add(kid)

    def __str__(self):
        return "Santa's List"
