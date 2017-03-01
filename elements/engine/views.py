from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpResponse


from rest_framework import generics, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from engine.models import Csv, Content
from engine.serializers import CsvSerializer, ContentSerializer

from engine.csv_to_db import CsvTodb



class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get(self, request, format=None):
        csv = Content.objects.all()
        serializer = ContentSerializer(csv, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContentSerializer(
            data=request.data, context={
                'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CsvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer


class ExportView(generics.ListAPIView):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer

    def get(self, request, format=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        #csv = Csv.objects.all()
        #serializer = CsvSerializer(csv, many=True)
        obj = CsvTodb()
        csv = obj.export()
        print (csv)
        return Response(obj.export())


class CsvList(generics.ListCreateAPIView):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer

    def get(self, request, format=None):
        csv = Csv.objects.all()
        serializer = CsvSerializer(csv, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CsvSerializer(
            data=request.data, context={
                'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
