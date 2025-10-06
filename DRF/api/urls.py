from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.employeesView,basename='employees')
urlpatterns = [
    # path('students/', views.studentsView),
    # path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.employeesView.as_view()),
    # path('employees/<int:pk>/', views.employeeDetailView.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.blogsView.as_view()),
    path('comments/',views.commentsView.as_view()),
    path('blogs/<int:pk>/',views.blogDetailView.as_view()),
    path('comments/<int:pk>/',views.commentDetailView.as_view()),
]