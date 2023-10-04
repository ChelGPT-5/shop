from itertools import product

from django.shortcuts import render
from catalog.models import Category, Product, Discount, Seller, Basket
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from catalog.serializers import (CategorySerializer, SellerSerializer,
                                 ProductSerializer, DiscountSerializer,
                                 AddProductSerializer, BasketSerializer, DeleteProductSerializer)
from django.db.models import F

class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer


class CategoryProductsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, category_id):
        queryset = Product.objects.filter(category__id=category_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class DiscountProductsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, discount_id):
        if discount_id == 0:
            queryset = Product.objects.filter(discount=None)
        else:
            queryset = Product.objects.filter(discount__id=discount_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class SellerProductsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, seller_id):
        queryset = Product.objects.filter(seller__id=seller_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class DiscountsListView(ListAPIView):
    queryset = Discount.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DiscountSerializer


class SellerListView(ListAPIView):
    queryset = Seller.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SellerSerializer


class BasketView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        input_serializer = AddProductSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        product = Product.object.get(id=input_serializer.data['product_id'])
        basket_object, _ = Basket.object.get_or_create(user=request.user, product=product)

        if basket_object.count:
            basket_object.count += input_serializer.data['count']
        else:
            basket_object.count = input_serializer.data['count']

        if basket_object.count <= 0:
            basket_object.delete()
        else:
            basket_object.save()

        basket_object.save()
        return Response()

    def get(self, request):
        user = request.user
        basket = Product.objects.prefetch_related('basket_set').filter(basket__user=user).values(
                "name", "price", "discount", count=F("basket_count"),
                discount_persent=F("discount__percent"),
                discount_date_end=F("discount__date_end"))

        serializer = BasketSerializer({"products": basket})
        return Response(serializer.data)

    def delete(self, request):
        input_serializer = DeleteProductSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        product = Product.objects.get(id=input_serializer.data['product_id'])
        Basket.objects.get(user=request.user, product=product).delete()
        return Response
