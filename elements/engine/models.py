import time

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# function for uploaded file path
def upload_path_handler(instance, filename):
    import os.path
    # do split filename->(filename , extention)
    fn, ext = os.path.splitext(filename)
    return "{date}/{date}_{timestamp}{ext}".format(
        date=instance.date, timestamp=int(
            time.time()), ext=ext)


class Csv(models.Model):
    """
    is_archived  : True  => csv contents has been successfully saved
    is_archived  : False => error ouccured

    error_status : 0    => no error
    error_status : 100  => file extention or format error
    error_status : 200  => csv header error
    """
    user = models.ForeignKey(User)
    file = models.FileField(null=True, upload_to=upload_path_handler)
    date = models.DateField(null=True)
    modified_at = models.DateField(auto_now=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True, null=True)
    is_archived = models.BooleanField()
    error_status = models.IntegerField(default=0, null=False)

    class Meta:
        managed = True
        db_table = "csvs"


class Content(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    image = models.CharField(max_length=255, null=False, blank=True)


    # get filtered contents by regular expression etc..
    @classmethod
    def get_clean_contents(self):
        pass

    def as_json(self):  # get JSON style data
        return(
            {
                "title": self.title,
                "description": self.description,
                "image": self.image,
            }
        )

    class Meta:
        managed = True
        db_table = "contents"
