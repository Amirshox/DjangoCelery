from django.urls import path

from .views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView, TaskResultAPIView

urlpatterns = [
    path('todo/', ItemListCreateAPIView.as_view()),
    path('todo/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('tasks/', TaskResultAPIView.as_view()),
]
