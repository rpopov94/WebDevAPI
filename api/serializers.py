from rest_framework.serializers import ModelSerializer
from api.models import DataMap

class DataMapSer(ModelSerializer):
    class Meta:
        model = DataMap
        fields = ['address', 'geoinfo', 'parks', 'stores', 'shools', 'kindergartens']