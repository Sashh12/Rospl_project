from django.db import models
from django.contrib.auth.models import User
import pickle
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.

# class YourModel(models.Model):
#     # Define your fields here
#     name = models.CharField(max_length=100)
CATEGORY_CHOICES=(
    ('BR','beverage '),
    ('BF','breakfast'),
    ('DT','dessert'),
    ('MC','main course'),
    ('SP','soup'),
    ('CH','chapati'),
)

# Create your models here.
STATE_CHOICES = (
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Daman and Diu','Daman and Diu'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Mizoram','Mizoram'),
    ('Meghalaya','Meghalaya'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    ProductId = models.CharField(max_length=20)
    food_name = models.CharField(max_length=100)
    #food_category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    food_category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.CharField(max_length=255)

    def __str__(self):
        return self.food_name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="You must have at least 1 guest."),
            MaxValueValidator(6, message="The maximum number of guests is 6.")  # Adjust as needed
        ]
    )
    message = models.TextField(blank=True,)

    def clean(self):
        # Ensure the reservation date is not in the past
        if self.date < timezone.now().date():
            raise ValidationError("The reservation date cannot be in the past.")

        # Ensure the time is during business hours (e.g., 9 AM to 10 PM)
        # if not (timezone.datetime(2024, 1, 1, 9, 0) <= timezone.datetime.combine(timezone.now(), self.time) <= timezone.datetime(2024, 1, 1, 22, 0)):
        #     raise ValidationError("Reservations can only be made between 9:00 AM and 10:00 PM.")

    def __str__(self):
        message_part = f" Message: {self.message}" if self.message else ""
        return f"{self.name} - {self.date} at {self.time.strftime('%I:%M %p')} for {self.guests} guest(s){message_part}"
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0,help_text = "Please enter 10 digits valid Number")
    pincode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    comment=models.TextField()
    def __str__(self):
        return self.name