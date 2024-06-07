from django.db import models


class Profile(models.Model):
    USER_CATEGORIES = [
        ("Bronze", "Bronze"),
        ("Silver", "Silver"),
        ("Gold", "Gold"),
        ("Platinum", "Platinum"),
        ("Diamond", "Diamond"),
    ]
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    client_category = models.CharField(
        max_length=10, choices=USER_CATEGORIES, default="Bronze"
    )
    country = models.CharField(max_length=100, default="")
    imagen = models.ImageField(upload_to="profile_pics", blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"[{self.first_name} {self.last_name}]"
