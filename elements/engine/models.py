import time
import re

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def upload_path_handler(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "{date}/{date}_{timestamp}{ext}".format(
        date=instance.date, timestamp=int(
            time.time()), ext=ext)


class Csv(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(null=True, upload_to=upload_path_handler)
    date = models.DateField(null=True)
    modified_at = models.DateField(auto_now=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True, null=True)
    is_archived = models.BooleanField()
    error_status = models.IntegerField(default=0,null=False) #100 wrong:header missing | 200 wrong:fileformat

    class Meta:
        managed = True
        db_table = "csvs"


class Content(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    image = models.CharField(max_length=255, null=False, blank=True)

    @classmethod
    def get_clean_contents(self):
        pass

    def as_json(self):
        return(
            {
                "title": self.title,
                "description": self.description,
                "image": self.image,
            }
        )

    def filepath(self):
        return "/".join(filter(lambda x: x, [self.type, self.file.name]))

    class Meta:
        managed = True
        db_table = "contents"
