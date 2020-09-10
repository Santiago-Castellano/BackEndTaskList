from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from Task.views.helps import Message,permission_denied


from Task.serializers import GroupTaskSerializer
from Task.models import GroupTask


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_group_task(request):

	group_task = GroupTask(user=request.user)
	serializer = GroupTaskSerializer(group_task, data=request.data)
	data = {}

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def detail_group_task(request,id):

	try:
		group_task = GroupTask.objects.get(id=id)
	except GroupTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

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
		return Response({'response': permission_denied('edit')}) 
		
	serializer = GroupTaskSerializer(group_task, data=request.data)
	data = {}

	if serializer.is_valid():
		serializer.save()
		data['response'] = Message.UPDATE_SUCCESS.value

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
		return Response({'response':permission_denied('delete')}) 

	operation = group_task.delete()
	data = {}

	if operation:
		data['response'] = Message.DELETE_SUCCESS.value

	return Response(data=data)
