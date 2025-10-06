from students.models import Student
from rest_framework import serializers
from employees.models import Employee
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

from blogs.models import Blog, Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True, read_only=True) 
    # Nested serializer to include comments we bring from related_name in models
    class Meta:
        model=Blog
        fields='__all__'

