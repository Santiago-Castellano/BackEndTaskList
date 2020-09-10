from django.contrib import admin
from Task.models import GroupTask, TypeTask, Task
# Register your models here.

admin.site.register(GroupTask)
admin.site.register(TypeTask)
admin.site.register(Task)