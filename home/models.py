from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Services(models.Model):
    title = models.CharField(max_length=300)
    logo = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    image = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=500)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.address1


class Newsletter(models.Model):
    email = models.EmailField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
