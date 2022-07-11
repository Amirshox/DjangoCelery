from django_celery_results.models import TaskResult
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer, TaskResultSerializer
from .services import create


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    def create(self, request, *args, **kwargs):
        create.delay(request.data)
        return Response(status=status.HTTP_200_OK, data={'message': 'The task has been sent for execution.'})


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TaskResultAPIView(ListAPIView):
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('status',)
    ordering_fields = ('date_done', 'date_created',)
    search_fields = ('task_id',)
