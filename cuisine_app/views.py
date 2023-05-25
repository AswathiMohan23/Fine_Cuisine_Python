import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cuisine_app.models import MenuModel
from cuisine_app.serializer import MenuSerializer, ItemSerializer


# Create your views here.
class Cuisine_Menu(APIView):
    serializer_class = MenuSerializer

    def post(self, request):
        logging.info("menu added")
        try:
            print(request.data)
            serializer = MenuSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "menu added", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        logging.info("menu retrieved")
        try:
            menu_data = MenuModel.objects.all()
            serializer = MenuSerializer(menu_data, many=True)
            return Response({"message": "Menu retrieved", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        logging.info("menu edited ")
        try:
            request.data.update({'user': request.user.id})
            menu_data = MenuModel.objects.get(id=request.data.get('id'), user=request.user)
            serializer = MenuSerializer(menu_data, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "menu  edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        logging.info("menu edited ")
        try:
            request.data.update({'user': request.user.id})
            menu_data = MenuModel.objects.get(id=request.data.get('id'), user=request.user)
            serializer = MenuSerializer(menu_data, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "menu  edited", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, menu_id):
        logging.info("menu deleted")

        try:
            menu_data = MenuModel.objects.get(id=menu_id)
            print(menu_data)
            menu_data.delete()
            return Response({"message": "menu deleted", "status": 200, "data": {}},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)

class CuisineItems(APIView):
    def post(self, request):
        logging.info("menu added")
        try:
            print(request.data)
            serializer = ItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "item added", "status": 200, "data": serializer.data},
                            status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception(e)
            return Response({"message": e.args[0], "status": 400, "data": {}},
                            status=status.HTTP_400_BAD_REQUEST)
