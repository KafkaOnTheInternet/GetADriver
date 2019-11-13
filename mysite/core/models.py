from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=20)
    birthdate = models.DateField()
    email = models.EmailField()
    location = models.CharField(max_length=100)

    def str(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=20)
    birthdate = models.DateField()
    email = models.EmailField()
    location = models.CharField(max_length=100)

    def str(self):
        return self.name


class Ride(models.Model):
    car = models.CharField(max_length=30)
    price = models.IntegerField()
    date = models.DateField()
    passenger_name = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE)



class RideDetails(models.Model):
    pass
    # passenger name
    # driver name
    # start date
    # end date
    # 



