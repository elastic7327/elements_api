#!/usr/bin/python
#-*- coding: utf-8 -*-

from __future__ import absolute_import
import re

from engine.models import Content

import pandas as pd


class CsvTodb(object):
    """
    error_status:100 => csvfileformat error
    error_status:200 => csvfileheader error
    """

    def __init__(self):
        self.is_archived = False
        self.error_status = 0

    def get_attr(self):
        return({
            "is_archived": self.is_archived,
            "error_status": self.error_status,
        })

    def to_db(self, file_obj):
        datas = []  # empty array for ORM bulk_create
        patterns = u"(title)|(description)|(image)"
        try:
            frame = pd.read_csv(file_obj).fillna(value="")
        except:
            self.error_status = 100
            return (self.get_attr())

        hlist = [
            col for col in frame.columns if re.match(
                patterns, u"{}".format(col))]
        filtered_frame = frame[hlist]
        if len(hlist) != 3:  # if matched header's length is not 3
            self.error_status = 200  # make it status to 200
            return (self.get_attr())

        for x in filtered_frame.iterrows():  # iterating PandasDataframe
            print(x[1][0], " " * 10, x[1][1], " " * 10, x[1][2])
            datas.append(
                Content(
                    title=x[1][0],
                    description=x[1][1],
                    image=x[1][2]))
        Content.objects.bulk_create(datas)

        self.is_archived = True
        return (self.get_attr())

    def export(self):
        query_set = Content.objects.all()
        frame = {"title": [], "image": [], "description": []}
        for x in query_set:
            frame["title"].append(x.title)
            frame["image"].append(x.image)
            frame["description"].append(x.description)
        df = pd.DataFrame.from_dict(frame)
        return (df.to_csv("output.csv"))

    def bulk_create(self, data):  # override bulk_create for exceptional condition
        if(data != []):
            klass = data[0].__class__
            res = klass.objects.bulk_create(data)

if __name__ == "__main__":
    pass
