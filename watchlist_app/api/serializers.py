from rest_framework import serializers
from watchlist_app.models import movie,watchlist,streamplateform,review
""" class movieserializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()
    def create(self,data):
     return  movie.objects.create(**data)
    def update(self,data,newdata):
       data.name=newdata.get('name',data.name)
       data.description=newdata.get('description',data.description)
       data.active=newdata.get('active',data.active)
       data.save()
       return data
        """
class reviewlistserializer(serializers.ModelSerializer):

    class Meta:
        model=review
        fields='__all__'

class watchlistserializer(serializers.ModelSerializer):
    reviews=reviewlistserializer(read_only=True,many=True)
    class Meta:
        model=watchlist
        fields='__all__'
        depth=1
    
class streamplateformerializer(serializers.ModelSerializer):
    watchlist= watchlistserializer(many=True,read_only=True)
    class Meta:
        model=streamplateform
        fields='__all__'

   