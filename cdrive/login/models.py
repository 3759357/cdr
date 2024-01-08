from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.CharField(db_column='user_id', max_length=50)
    passwd = models.CharField(db_column='passwd',max_length=50)
    name = models.CharField(db_column='name',max_length=50)
    email = models.CharField(db_column='email',max_length=50)
    mbti = models.CharField(db_column='mbti',max_length=50)
    

    class Meta:

        db_table='user';


class Bookmark(models.Model):
    user_id = models.CharField(db_column='user_id', max_length=50)
    place = models.CharField(db_column='place', max_length=50)
    rating = models.CharField(db_column='rating', max_length=50)
    stamp = models.IntegerField(db_column='stamp', default=0)

    class Meta:
        db_table = 'bookmark';

class marker(models.Model):
    place = models.CharField(db_column='place', max_length=50)
    parking = models.CharField(db_column='parking', max_length=50)
    address = models.CharField(db_column='address', max_length=50)
    rating = models.CharField(db_column='rating', max_length=50)
    lat = models.CharField(db_column='lat', max_length=50)
    lng = models.CharField(db_column='lng', max_length=50)
