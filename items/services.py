from celery import shared_task

from .serializers import ItemSerializer


@shared_task(name='Create Item')
def create(data):
    serializer = ItemSerializer(data=data)
    is_valid = serializer.is_valid()
    if is_valid:
        serializer.save()
    return {'data': serializer.data, 'error': serializer.errors, 'is_valid': is_valid}
