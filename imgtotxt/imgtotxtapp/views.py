from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import cv2
import pybase64
import pytesseract
from django.views.decorators.http import require_POST

__file_name = 'test.png'


@require_POST
@api_view(['POST'])
def sendfileinbase64(base64request):
    decoded_base64 = pybase64.b64decode(base64request.data)
    try:
        file = open(__file_name, 'wb')
        file.write(decoded_base64)
        file.close()
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    try:
        img = cv2.imread(__file_name)

        txt = pytesseract.image_to_string(img, lang='eng')
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    return Response(txt)
