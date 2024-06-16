from django.db import models

class Patient(models.Model):

    """
    Patient
    Stores a single patient entry for every report
    """

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ["forename", "surname"]

    def __str__(self):
        return f'{self.forename} {self.surname}'
    
    surname = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=50)
    sample_number = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    lab_no = models.CharField(max_length=30)
    sample_dated = models.CharField(max_length=50)
    sample_received = models.CharField(max_length=50)
    result_reported = models.CharField(max_length=50)
    sample_type = models.CharField(max_length=255)

class Summary(models.Model):
    
        """
        Summary
        Stores a single summary entry related to a patient.
        """
    
        class Meta:
            verbose_name = 'Summary'
            verbose_name_plural = 'Summaries'
    
        def __str__(self):
            return f'{self.user.forname} - {self.summary[:50]}'
        
        user = models.ForeignKey(Patient, on_delete=models.CASCADE)
        summary = models.TextField()


    
class TestResult(models.Model):

    """
    TestResult
    Stores a single TestResult entry related to a patient.
    """

    class Meta:
        verbose_name = 'TestResult'
        verbose_name_plural = 'TestResults'
        ordering = ["test_name"]

    def __str__(self):
        return f'{self.user.forename} - {self.test_name}'
    
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=20, decimal_places=2, null=True, default=0)
    unit = models.CharField(max_length=100)
    ref_range = models.CharField(max_length=255, null=True, default='')
    explanation = models.TextField()
