import datetime

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import cv2
import pybase64
import pytesseract
import numpy as np


def home(request):
    return HttpResponse("Response form home request here!!")


@api_view(['POST'])
def sendfileinbase64(base64request):
    decoded_base64 = pybase64.b64decode(base64request.data)

    file = open('test.png', 'wb')
    file.write(decoded_base64)
    file.close()

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread('test.png')

    txt = pytesseract.image_to_string(img, lang='eng')

    return Response(txt)



@api_view(['POST'])
def test(request):
    return Response(request.data)







