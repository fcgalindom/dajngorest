
from polls.api.serilice import QuetionSerialice
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import serializers
from rest_framework import status
from polls.models import Question






@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
@api_view(['POST'])
def add_items(request):
    question = QuetionSerialice(data=request.data)

    # validating for already existing data
    if Question.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if question.is_valid():
        question.save()
        return Response(question.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    item = Question.objects.get(pk=pk)
    data = QuetionSerialice(instance=item, data=request.data)


    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Question.objects.filter(**request.query_param.dict())
    else:
        items = Question.objects.all()

    # if there is something in items else raise error
    if items:
        data = QuetionSerialice(items,many=True)
        respuesta = data.data
        return Response(respuesta)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = Question.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)