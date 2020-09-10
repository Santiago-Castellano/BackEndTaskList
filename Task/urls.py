from django.urls import path
import Task.views.group_task as group_task


urlpatterns = [
    path('create_group_task/',group_task.create,name='create_group_task'),
    path('<id>/update_group_task',group_task.update,name='update_group_task'),
    path('<id>/detail_group_task',group_task.detail,name='detail_group_task'),
    path('<id>/delete_group_task',group_task.delete,name='delete_group_task')
]