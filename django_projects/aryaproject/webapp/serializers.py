from rest_framework import serializers

from .models import employee

class employeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = employee

        #fields = ('firstname','lastname')
    
        fields = '__all__'
