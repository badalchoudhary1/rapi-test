from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404




class StudentView(APIView):
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        

    def get(self,request,*args,**kwargs):
        result=Students.objects.all()
        serializers=StudentSerializer(result,many=True)
        return Response({"status":"success","students":serializers.data},status=200)
    
    def delete(self,request,id=None):
        result=get_object_or_404(Students,id=id)
        result.delete()
        return Response({"status":"success","data":"record deleted"})
    
    def put(self,request,id):
        person=Students.objects.get(id=id)
        serializer=StudentSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"success","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        person=Students.objects.get(id=id)
        studentData=StudentSerializer(instance=person,data=request.data,partial=True)


        if studentData.is_valid():
            studentData.save()
            return Response(studentData.data)
        
        else:
            return Response(status=status.HTTP_484_NOT_FOUND)    
    