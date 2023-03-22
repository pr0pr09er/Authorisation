from django.urls import path
from .views import (
    get_student, get_students, create_student, update_student, delete_student, get_subjects, get_subject,
    create_subject, update_subject, delete_subject, get_classes, get_class, create_class, update_class, delete_class
)

urlpatterns = [
    # Student
    path('students/', get_students, name='students-list'),
    path('students/<int:pk>/', get_student, name='students-detail'),
    path('create_student/', create_student, name='create-student'),
    path('delete_student/<int:pk>/', delete_student, name='delete-student'),
    path('update_student/<int:pk>/', update_student, name='update-student'),
    # Subject
    path('subjects/', get_subjects, name='subjects-list'),
    path('subjects/<int:pk>/', get_subject, name='subjects-detail'),
    path('create_subject/', create_subject, name='create-subject'),
    path('delete_subject/<int:pk>/', delete_subject, name='delete-subject'),
    path('update_subject/<int:pk>/', update_subject, name='update-subject'),
    # Class
    path('classes/', get_classes, name='classes-list'),
    path('classes/<int:pk>/', get_class, name='classes-detail'),
    path('create_class/', create_class, name='create-class'),
    path('delete_class/<int:pk>/', delete_class, name='delete-class'),
    path('update_class/<int:pk>/', update_class, name='update-class'),
]
