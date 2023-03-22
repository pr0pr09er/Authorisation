from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Student, Class, Subjects
from .serializers import SubjectsSerializer, StudentSerializer, ClassSerializer


# student
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response({"students": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)

    return Response({"student": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_student(request):
    serializer = StudentSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(data=request.data, instance=student)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()

    return Response({"response": "instance deleted"}, status=status.HTTP_200_OK)


# subject
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subjects(request):
    students = Subjects.objects.all()
    serializer = SubjectsSerializer(students, many=True)

    return Response({"students": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subject(request, pk):
    try:
        subject = Subjects.objects.get(id=pk)
    except Subjects.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubjectsSerializer(subject)

    return Response({"student": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_subject(request):
    serializer = SubjectsSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_subject(request, pk):
    try:
        subject = Subjects.objects.get(id=pk)
    except Subjects.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubjectsSerializer(data=request.data, instance=subject)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_subject(request, pk):
    try:
        subjects = Subjects.objects.get(id=pk)
    except Subjects.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    subjects.delete()

    return Response({"response": "instance deleted"}, status=status.HTTP_200_OK)


# class
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_classes(request):
    classes = Class.objects.all()
    serializer = SubjectsSerializer(classes, many=True)

    return Response({"students": serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_class(request, pk):
    try:
        classs = Class.objects.get(id=pk)
    except Class.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubjectsSerializer(classs)

    return Response({"student": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_class(request):
    serializer = ClassSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_class(request, pk):
    try:
        classs = Class.objects.get(id=pk)
    except Class.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClassSerializer(data=request.data, instance=classs)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({"data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_class(request, pk):
    try:
        classs = Class.objects.get(id=pk)
    except Class.DoesNotExist:
        return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    classs.delete()

    return Response({"response": "instance deleted"}, status=status.HTTP_200_OK)
