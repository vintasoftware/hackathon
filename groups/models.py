from django.conf import settings
from django.db import models
from model_utils import Choices
from taggit.managers import TaggableManager



class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   through='GroupMembership')

    def __str__(self):
        return self.name


class Link(models.Model):
    TYPES = Choices('link', 'article', 'video')
    url = models.URLField()
    title = models.CharField(max_length=750, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True, default=0)
    group = models.ForeignKey(Group)
    media_type = models.CharField(choices=TYPES, max_length=255,
                                  default=TYPES.link)

    tags = TaggableManager()

    def __str__(self):
        return self.url


class GroupMembership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    is_creator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'group'),)
