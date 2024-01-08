from rest_framework import serializers
from .models import user,Bookmark

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields='__all__'

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='get_info', lookup_field='id', read_only=True)
    class Meta:
        model = Bookmark
        fields='__all__'