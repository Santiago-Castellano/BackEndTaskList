from rest_framework import serializers
from Task.models import TypeTask

class TypeTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeTask
        fields = ['id', 'name', 'color', 'group__id']
        read_only_fields = ['group__id']
        
