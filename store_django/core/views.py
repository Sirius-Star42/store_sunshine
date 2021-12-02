from rest_framework.views import APIView
from django.http import Http404
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Products
from .serializers import ProductsSerializers

class ProductsAPIView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    
    def get(self,format=None):
        products =  Products.objects.all()
        serializer = ProductsSerializers(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data has been created',status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ProductDetailOprs(APIView):
    def get_object(self,pk):
        try:
            return Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response('Selected item deleted', status=status.HTTP_204_NO_CONTENT)


