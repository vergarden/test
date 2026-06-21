from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BoardSaying, EmailSending
from .serializers import BoardSayingSerializer, EmailSendingSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        'message': '欢迎使用 Vue + Django 应用！',
        'admin_url': '/admin/',
    })


@api_view(['GET'])
def boardsaying_count(request):
    count = BoardSaying.objects.count()
    return Response({'count': count})


@api_view(['GET', 'POST'])
def boardsaying_list(request):
    if request.method == 'GET':
        msgs = BoardSaying.objects.all().order_by('?')[:3]
        serializer = BoardSayingSerializer(msgs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BoardSayingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def emailsending_create(request):
    serializer = EmailSendingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
