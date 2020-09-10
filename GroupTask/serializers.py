from rest_framework import serializers
from GroupTask.models import GroupTask

class GroupTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTask
        fields = [ 'id','name' ]