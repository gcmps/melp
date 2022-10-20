from django.db import models


class Restaurant(models.Model):

    id = models.AutoField(
        primary_key=True,
        unique=True,
    )

    rating = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=0) & models.Q(rating__lte=4),
                name="Number between 0 and 4",
            )
        ]

    name = models.CharField(max_length=50)

    site = models.CharField(max_length=100)

    email = models.CharField(max_length=50)

    phone = models.CharField(max_length=50)

    street = models.CharField(max_length=50)

    city = models.CharField(max_length=50)

    state = models.CharField(max_length=50)

    lat = models.FloatField()

    lng = models.FloatField()

    def __str__(self):
        return self.name
