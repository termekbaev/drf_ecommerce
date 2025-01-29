from django.db import models

from apps.accounts.models import User
from apps.common.models import BaseModel


class ShippingAddress(BaseModel):
    """
    Represents a shipping address associated with a user.

    Attributes:
        user (ForeignKey): The user who owns the shipping address.
        full_name (str): The full name of the recipient.
        email (str): The email address of the recipient.
        phone (str): The phone number of the recipient.
        address (str): The street address of the recipient.
        city (str): The city of the recipient.
        country (str): The country of the recipient.
        zipcode (int): The postal code of the recipient.

    Methods:
        __str__():
            Returns a string representation of the shipping details.
   """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_addresses")
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=1000, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    zipcode = models.ImageField(null=True)

    def __str__(self):
        return f"{self.full_name}'s shipping details"