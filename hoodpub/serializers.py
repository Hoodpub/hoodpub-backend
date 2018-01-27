from rest_framework import serializers
from hoodpub.models import Hoodpub


class HoodpubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hoodpub
        fields = '__all__'
