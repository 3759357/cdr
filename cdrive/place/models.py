from django.db import models

# Create your models here.

class tour(models.Model):
    place = models.CharField(db_column='place', max_length=50)
    parking = models.CharField(db_column='parking', max_length=50)
    parking_lot = models.CharField(db_column='parking_lot', max_length=50)
    rating = models.CharField(db_column='rating', max_length=50)

    class Meta:
        db_table = 'tour';

class restaurant(models.Model):
    place = models.CharField(db_column='place', max_length=50)
    parking = models.CharField(db_column='parking', max_length=50)
    parking_lot = models.CharField(db_column='parking_lot', max_length=50)
    rating = models.CharField(db_column='rating', max_length=50)

    class Meta:
        db_table = 'restaurant';