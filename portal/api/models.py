from django.db import models

class CandidateDetails(models.Model):
    first_name = models.CharField(max_length=200,null=False,default="Please enter your first name")
    last_name = models.CharField(max_length=200,null=False,default="Please enter your last name")
    email = models.CharField(max_length=255,unique=True)
    dob = models.DateField(null=False,default="Please enter your DOB")
    highest_qualification = models.CharField(max_length=200,null=False,default="Please enter your highest qualification")
    stream = models.CharField(max_length=200,null=False,default="Enter your stream")
    ssc = models.IntegerField(null=False,default="Enter your 10th marks")
    inter = models.IntegerField(null=False,default="enter your 12 th marks")
    bachelor = models.IntegerField(null=True)
    height = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    eye_sight = models.FloatField(null=True)
    disorder = models.CharField(max_length=200,null=True)
    nationality = models.CharField(max_length=200,null=False)

    def __str__(self):
        return  self.first_name