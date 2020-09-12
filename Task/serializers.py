from rest_framework import serializers
from Task.models import GroupTask,TypeTask

class GroupTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTask
        fields = [ 'id','name' ]

class TypeTaskSerializer(serializers.ModelSerializer):
    group = GroupTaskSerializer(read_only= True)
    class Meta:
        model = TypeTask
        fields = ['id', 'name', 'color', 'group']
        
