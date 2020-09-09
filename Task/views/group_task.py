from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from Task.serializers import GroupTaskSerializer
from Task.models import GroupTask


SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def detail_group_task(request,id):

	try:
		group_task = GroupTask.objects.get(id=id)
	except GroupTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = GroupTaskSerializer(group_task)
		return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update_group_task(request, id):

	try:
		 group_task= GroupTask.objects.get(id=id)
	except GroupTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if group_task.user != user:
		return Response({'response':"You don't have permission to edit that."}) 
		
	if request.method == 'PUT':
		serializer = GroupTaskSerializer(group_task, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = UPDATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
def delete_group_task(request,id):

	try:
		group_task = GroupTask.objects.get(id=id)
	except GroupTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if group_task.user != user:
		return Response({'response':"You don't have permission to delete that."}) 

	if request.method == 'DELETE':
		operation = group_task.delete()
		data = {}
		if operation:
			data['response'] = DELETE_SUCCESS
		return Response(data=data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_group_task(request):

	group_task = GroupTask(user=request.user)

	if request.method == 'POST':
		serializer = GroupTaskSerializer(group_task, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
