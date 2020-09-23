from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GroupTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)


class TypeTask(models.Model):
    group = models.ForeignKey(GroupTask, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)


class Task(models.Model):
    group = models.ForeignKey(GroupTask, on_delete=models.CASCADE)
    type_task = models.ForeignKey(TypeTask, on_delete=models.CASCADE)
    to_do = models.CharField(max_length=350)
    ended_by = models.ManyToManyField(User)


class GroupShared(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupTask, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'group'),)
