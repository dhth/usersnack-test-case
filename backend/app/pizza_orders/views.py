from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination

from .models import Movie, FoodItem, Order, OrderDetail
from django.db.models import ExpressionWrapper, F, DecimalField
from django.shortcuts import get_object_or_404
from .serializers import (
    MovieSerializer,
    PizzaSerializer,
    ExtraSerializer,
    CreateOrderSerializer,
    OrderDetailResponseSerializer,
    OrderSerializer,
)
from decimal import Decimal
from django.core.paginator import Paginator
from usersnack import settings as app_settings

from django.http import JsonResponse
from . import util


class PizzaList(APIView):
    def get(self, request, format=None):

        page_num = int(request.GET.get("page_num", 1))
        pizzas = FoodItem.objects.filter(item_type="pizza").order_by("id")
        paginator = Paginator(pizzas, app_settings.DEFAULT_PAGINATION_SIZE)
        if page_num > paginator.num_pages:
            util.log(
                "error",
                message="Pizza List: Page Num Exceeded",
                context={
                    "page_num": page_num,
                    "total_pages": paginator.num_pages,
                },
            )
            return JsonResponse(
                {"success": False, "detail": "page_num exceeded limit"}
            )
        pizzas_page = paginator.page(page_num)
        serializer = PizzaSerializer(pizzas_page, many=True)
        return JsonResponse({"success": True, "pizzas": serializer.data})


class ExtraList(APIView):
    def get(self, request):
        extras = FoodItem.objects.filter(item_type="extra").order_by("id")
        serializer = ExtraSerializer(extras, many=True)
        return JsonResponse({"success": True, "extras": serializer.data})


class CreateOrder(APIView):
    """
    Create a order
    """

    def post(self, request, format=None):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            new_order = serializer.save()
            if new_order is not None:
                new_order_serialized = OrderSerializer(new_order, many=False)
                return JsonResponse(
                    {"success": True, "order": new_order_serialized.data,}
                )
            return JsonResponse(
                {"success": False, "detail": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        else:
            util.log(
                "error",
                message="Error Creating order",
                context={
                    "request_data": request.data,
                    "errors": serializer.errors,
                },
            )
            return JsonResponse(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class OrderDetailView(APIView):
    def get_order_components(self, pk):
        order_obj = get_object_or_404(Order, pk=pk)
        try:
            return (
                OrderDetail.objects.filter(order_id=pk)
                .values("food_item__name", "food_item__item_type", "quantity",)
                .annotate(
                    amount=ExpressionWrapper(
                        F("food_item__price") * F("quantity"),
                        output_field=DecimalField(),
                    )
                )
            )
        except Exception as e:
            util.log(
                "error",
                message="Error fetching order details",
                context={"pk": pk, "error": str(e),},
            )
            raise Http404

    def get(self, request, pk, format=None):
        order_components = self.get_order_components(pk)
        total = 0
        for order_component in order_components:
            total += Decimal(order_component["amount"])
        serializer = OrderDetailResponseSerializer(order_components, many=True)
        return JsonResponse(
            {
                "success": True,
                "order_id": pk,
                "order_items": serializer.data,
                "total": total,
            }
        )


class OrderListView(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({"success": True, "orders": serializer.data})
