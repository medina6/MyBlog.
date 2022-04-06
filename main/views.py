from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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



# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])      # router builds path posts/search/q=paris
    def search(self, request, pk=None):
        q = request.query_params.get('q')             #request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q) |
                                   Q(text__icontains=q))
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostImageView(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}

###
