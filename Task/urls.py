from django.urls import path
import Task.views.group_task as group_task


urlpatterns = [
    path('create_group_task/',group_task.create,name='create_group_task'),
    path('update_group_task/<int:id>',group_task.update,name='update_group_task'),
    path('detail_group_task/<int:id>',group_task.detail,name='detail_group_task'),
    path('delete_group_task/<int:id>',group_task.delete,name='delete_group_task')
]