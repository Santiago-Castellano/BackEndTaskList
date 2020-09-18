from django.urls import path
import Task.views.group_task as group_task
import Task.views.type_task as type_task

urlpatterns = [
    #Group Task
    path('group/create/'        ,group_task.create,name='create_group_task'),
    path('group/update/<int:pk>',group_task.update,name='update_group_task'),
    path('group/detail/<int:pk>',group_task.detail,name='detail_group_task'),
    path('group/delete/<int:pk>',group_task.delete,name='delete_group_task'),

    #Type Tasl
    path('type/create/<int:pk_group>' ,type_task.create,name='create_type_task'),
    path('type/update/<int:pk>'       ,type_task.update,name='update_type_task'),
    path('type/detail/<int:pk>'       ,type_task.detail,name='detail_type_task'),
    path('type/delete/<int:pk>'       ,type_task.delete,name='delete_type_task'),

]
