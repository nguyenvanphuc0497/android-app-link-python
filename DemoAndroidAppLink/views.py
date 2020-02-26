from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_file_asset(request):
    return FileResponse(open('assetlinks.json', 'rb'), status=status.HTTP_200_OK, content_type='application/json')


# @api_view(['GET'])
# def get_file_asset(request):
#     return Response(open('assetlinks.json', 'rb'), status=status.HTTP_200_OK, content_type='application/json')
