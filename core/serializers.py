from rest_framework import serializers
from .models import Patient, Summary, TestResult

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'


class SummarySerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
        model = Summary
        fields = '__all__'


class TestResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestResult
        fields = '__all__'