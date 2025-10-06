'''from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from students.models import Student
def studentsView(request):
    # students={
    #     'id':1,
    #     'name':'John Doe',  
    #     'age':21,   
    #     'course':'Computer Science'
    # }
    students=Student.objects.all().values()  #queryset
    students=list(students)  #convert queryset to list
    return JsonResponse(students, safe=False)  #safe false for non dictionary objects

# Using Django REST Framework function based views

from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)  #safe false for non dictionary objects
    elif request.method == 'POST':  #create new student
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error':'Student not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':  #update student
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  #delete student
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Class Based Views without Mixins 

from employees.models import Employee
from .serializers import EmployeeSerializer 
from rest_framework.views import APIView

class employeesView(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class employeeDetailView(APIView):
    def get(self,request,pk):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Class Based Views with Mixins
        
from rest_framework import generics,mixins
from employees.models import Employee
from .serializers import EmployeeSerializer

class employeesView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class employeeDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

#Generic class based views

from rest_framework import generics
from employees.models import Employee
from .serializers import EmployeeSerializer

class employeesView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class employeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer



#ViewSets

from rest_framework import viewsets
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

class employeesView(viewsets.ViewSet):
    def list(self,request):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        try:
            employee=Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

#ViewSets ModelViewSets
from rest_framework import viewsets
from employees.models import Employee   
from .serializers import EmployeeSerializer
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
class employeesView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=CustomPagination
    # filterset_fields = ['department', 'name']
    filterset_class = EmployeeFilter
   


from rest_framework import generics
from blogs.models import Blog,Comment
from .serializers import CommentSerializer,BlogSerializer
class blogsView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class commentsView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class blogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'
class commentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'