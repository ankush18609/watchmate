from watchlist_app.models import movie,watchlist,streamplateform,review
from watchlist_app.api.serializers import watchlistserializer,streamplateformerializer,reviewlistserializer
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics
"""
@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movies=movie.objects.all()
        serializer=movieserializer(movies,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def get_by_id(request,pkey):
    if request.method=='GET':
        movies=movie.objects.get(pk=pkey)
        serializer=movieserializer(movies)
        return Response(serializer.data)
    elif request.method=='PUT':
        movies=movie.objects.get(pk=pkey)
        serializer=movieserializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    #elif request.method=='DELETE':
   ## movies=movie.objects.get(pk=pkey)
    #serializer=movieserializer(movies)
   ## return Response(serializer.data)"""
"""class movie_list(APIView):
    def get(self,request):
        movies=movie.objects.all()
        serializer=movieserializer(movies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
class Movie_by_id(APIView):
    def get(self,request,pkey):
        movies=movie.objects.get(pk=pkey)
        serializer=movieserializer(movies)
        return Response(serializer.data)
    def put(self,request,pkey):
        movies=movie.objects.get(pk=pkey)
        serializer=movieserializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self,request,pkey):
        movies=movie.objects.get(pk=pkey)
        serializer=movieserializer(movies)
        movies.delete()
        return Response(serializer.data)"""

class WatchListAv(APIView):
    def get(self,request):
        watchlists=watchlist.objects.all()
        serializer=watchlistserializer(watchlists,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=watchlistserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class streamplateformAv(APIView):
    def get(self,request):
        streamplateforms=streamplateform.objects.all()
        serializer=streamplateformerializer(streamplateforms,many=True,context={'request': request})
        return Response(serializer.data)
    def post(self,request):
        serializer=streamplateformerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class watchlistDetail(APIView):
    def get(self,request,pkey):
        try:
            watchlists=watchlist.objects.get(pk=pkey)
        except watchlist.DoesnotExist:
            return Response({'movie not found'},status=status.HttpStatus.NOT_FOUND)
        serializer=watchlistserializer(watchlists)
        return Response(serializer.data)  
    def put(self,request,pkey):
        watchlists=watchlist.objects.get(pk=pkey)
        serializer=watchlisterializer(watchlists,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,pkey):
        try:
            watchlists=watchlist.objects.get(pk=pkey)
        except watchlist.DoesnotExist:
            return Response({'movie not found'},status=status.HttpStatus.NOT_FOUND)
        watchlists.delete()
        return Response(serializer.data)
class streamplateformDetail(APIView):
    def get(self,request,pk):
        try:
            streamplateforms=streamplateform.objects.get(pk=pk)
        except streamplateform.DoesnotExist:
            return Response({'movie not found'},status=status.HttpStatus.NOT_FOUND)
        serializer=streamplateformerializer(streamplateforms)
        return Response(serializer.data)
    def put(self,request,pk):
        streamplateforms=streamplateform.objects.get(pk=pk)
        serializer=streamplateformerializer(streamplateforms,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializers.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        try:
            streamplateforms=streamplateform.objects.get(pk=pk)
        except streamplateform.DoesnotExist:
            return Response({'movie not found'},status=status.HttpStatus.NOT_FOUND)
        streamplateforms.delete()
        return Response(serializers.data)
class reviewlistav(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
      queryset = review.objects.all()
      serializer_class = reviewlistserializer

      def get(self, request, *args, **kwargs):
         return self.list(request, *args, **kwargs)

      def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)
class reviewdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
      queryset = review.objects.all()
      serializer_class = reviewlistserializer

      def get(self, request, *args, **kwargs):
         return self.retrieve(request, *args, **kwargs)

      def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs)

      def delete(self, request, *args, **kwargs):
         return self.destroy(request, *args, **kwargs)
    



