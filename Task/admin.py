from django.contrib import admin
from Task.models import  TypeTask, Task,GroupShared
# Register your models here.

admin.site.register(TypeTask)
admin.site.register(Task)
admin.site.register(GroupShared)