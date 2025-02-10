from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

import pandas
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Create your views here.
class NormalizationController(viewsets.ViewSet):

    def requestNormalize(self, request):
        print("데이터 준비")
        data = {
            'Age': [25, 30, 35, None, 40],
            'Gender': ['MAN', 'WOMAN'],
        }