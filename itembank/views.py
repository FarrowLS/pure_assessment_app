from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from itembank.models import Item
from itembank.serializers import ItemSerializer
        

@api_view(['GET', 'POST'])
def item_list(request):
    """
    List all the items or create a new item
    """
    if request.method == 'GET':
        current_items = Item.objects.all()
        serializer = ItemSerializer(current_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        current_item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(current_item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(current_item, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        current_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)