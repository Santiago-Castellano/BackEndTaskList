from rest_framework import serializers
from models import GroupTask

class GroupTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTask
        fields = [ 'name' ]
        
