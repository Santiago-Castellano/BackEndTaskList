from rest_framework import serializers
from Task.models import GroupTask

class GroupTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTask
        fields = [ 'name' ]
        
