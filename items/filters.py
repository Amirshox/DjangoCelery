from django_filters import FilterSet, BooleanFilter

from django_celery_results.models import TaskResult


# class TaskResultFilter(FilterSet):
#     is_valid = BooleanFilter(field_name='result__is_valid')
#
#     class Meta:
#         model = TaskResult
#         fields = {
#             'is_valid': ['exact'],
#         }
