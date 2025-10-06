import django_filters
from .models import Employee
class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(lookup_expr='iexact',field_name='department')
    name=django_filters.CharFilter(lookup_expr='icontains',field_name='name')
    class Meta:
        model = Employee
        fields=['department', 'name']