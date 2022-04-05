from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics

from main.models import Category, Post, PostImage
from .serializers import CategorySerializer, PostSerializer, PostImageSerializer
# #
# #
# @api_view(['GET'])
# def categories(request):
# # #     # if request.method == "GET":
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True) # formotiruet vse dannye
#         return Response(serializer.data)   # Zdes hranyatsya dannye posle formatirovnaie
#     # else:
#     #     return Response({"message": "Hello makers Bootcamp!"})
#
#
# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
# # #
#     def post(self, request):
#         post = request.data
#         serializer = PostSerializer(data=post)
#         if serializer.is_valid(raise_exception=True):
#             post_saved = serializer.save()
#         return Response(serializer.data)
from main.models import Category, Post
from main.serializers import CategorySerializer, PostSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


