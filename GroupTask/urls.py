from django.urls import path
from GroupTask.views import create,update,delete,detail

urlpatterns = [
    path('create/'        ,create,name='create_group_task'),
    path('update/<int:id>',update,name='update_group_task'),
    path('detail/<int:id>',detail,name='detail_group_task'),
    path('delete/<int:id>',delete,name='delete_group_task'),
]