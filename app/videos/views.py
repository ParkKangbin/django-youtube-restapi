from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoListSerializers, VideoDetailSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#Video와 관련된 REST API 전체 적인 조회(GET) 
#새로운 비디오 생성[POST]
class VideoList(APIView):
    def get(self,request):
        videos = Video.objects.all() # objects = 쿼리셋 [Video,Video,Video,Video,]

        serializer = VideoListSerializers(videos,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        user_data = request.data

        serializer = VideoListSerializers(data=user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



from rest_framework.exceptions import NotFound
# 특정한 조회 업데이트 삭제 까지 3가지 
class VideoDetail(APIView):
    def get(self,requset,pk):
        try:
            video_obj = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            raise NotFound
        serializer = VideoDetailSerializer(video_obj)

        return Response(serializer.data,200)
    def put(self,requset,pk):
        video_obj = Video.objects.get(pk=pk)
        user_data = requset.data

        serializer = VideoDetailSerializer(video_obj,user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self,requset,pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    