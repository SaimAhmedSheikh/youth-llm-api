from rest_framework import permissions, viewsets
from .models import Patient, Summary, TestResult
from .serializers import PatientSerializer, SummarySerializer, TestResultSerializer
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class SummaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows summaries to be viewed or edited.
    """
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class TestResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows test results to be viewed or edited.
    """
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer