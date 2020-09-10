from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Task.models import TypeTask,GroupTask
from Task.serializers import TypeTaskSerializer
from Task.views.helps import Message


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create(request):
    type_task = TypeTask(user=request.user)
    serializer = TypeTaskSerializer(type_task, data=request.data)

    if correct_group(type_task.id_group,request.user):
	    return Response(status=status.HTTP_404_NOT_FOUND)

    if serializer.is_valid():
	    serializer.save()

	    return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def detail(request,id):
	try:
		type_task = TypeTask.objects.get(id=id)
	except TypeTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if correct_group(type_task.id_group,request.user):
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = TypeTaskSerializer(type_task)

	return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update(request, id):
	try:
		 type_task= TypeTask.objects.get(id=id)
	except TypeTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if correct_group(type_task.id_group,request.user):
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	serializer = TypeTaskSerializer(type_task, data=request.data)
	data = {}

	if serializer.is_valid():
		serializer.save()
		data['response'] = Message.UPDATE_SUCCESS.value

		return Response(data=data)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
def delete(request,id):
	try:
		type_task = TypeTask.objects.get(id=id)
	except TypeTask.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if correct_group(type_task.id_group,request.user):
		return Response(status=status.HTTP_404_NOT_FOUND)

	operation = type_task.delete()
	data = {}

	if operation:
		data['response'] = Message.DELETE_SUCCESS.value

	return Response(data=data)

def correct_group(id_group,user):
    try:
        group = GroupTask.objects.get(id=id_group,user=user)
        return True
    except Persona.DoesNotExist:
        return False