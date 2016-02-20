from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Link(models.Model):
    url = models.URLField()
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.url
