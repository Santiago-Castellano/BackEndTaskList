from django.urls import path
import Task.views.group_task as group_task

urlpatterns = [
    #Group Task
    path('group/create/'        ,group_task.create,name='create_group_task'),
    path('group/update/<int:pk>',group_task.update,name='update_group_task'),
    path('group/detail/<int:pk>',group_task.detail,name='detail_group_task'),
    path('group/delete/<int:pk>',group_task.delete,name='delete_group_task'),

]
