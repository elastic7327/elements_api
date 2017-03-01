#!/usr/bin/python
#-*- coding: utf-8 -*-
from __future__ import absolute_import

from rest_framework import serializers

from engine.models import Csv, Content
from engine.csv_to_db import CsvTodb


class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csv
        fields = (
            'id',
            'user',
            'date',
            'uploaded_at',
            'file',
            'modified_at',
            'is_archived',
            'error_status')

    def create(self, validated_data):
        user = validated_data.get('user', None)
        date = validated_data.get('date', None)
        file = validated_data.get('file', None)
        is_archived = validated_data.get('is_archived', None)
        uploaded_at = validated_data.get('uploaded_at', None)
        modified_at = validated_data.get('modified_at', None)
        error_status = validated_data.get('error_status', None)

        # assign core module instance
        ctd = CsvTodb()

        # call ctd object's to_db method
        # then throw file argument
        res = getattr(ctd, 'to_db')(file)

        return Csv.objects.create(
            user=user,
            date=date,
            file=file,
            uploaded_at=uploaded_at,
            is_archived=res["is_archived"],  # assign CTB module's result
            modified_at=modified_at,
            error_status=res["error_status"]  # assign CTB module's result
        )


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'image')
        model = Content
