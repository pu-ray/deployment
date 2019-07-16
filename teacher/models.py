from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=70)
    date_joined = models.DateField()
    proffessional = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    id_number = models.SmallIntegerField(null=True)
    image = models.ImageField(upload_to="profile_image",blank=True)


    def __str__(self):
        return self.first_name
        