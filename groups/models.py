from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=750, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.url
