from django.urls import path
import Task.views.type_task as type_task 


urlpatterns = [
    path('type/create/',        type_task.create,name='create_type_task'),
    path('type/update/<int:id>',type_task.update,name='update_type_task'),
    path('type/detail/<int:id>',type_task.detail,name='detail_type_task'),
    path('type/delete/<int:id>',type_task.delete,name='delete_type_task')
]