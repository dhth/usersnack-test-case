from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination

from .models import Movie, FoodItem
from .serializers import (
    MovieSerializer,
    PizzaSerializer,
    ExtraSerializer,
    OrderSerializer,
)

from django.core.paginator import Paginator
from usersnack import settings as app_settings

# Create your views here.
from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


class MovieList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 5


class PizzaList(APIView):
    # pagination_class = StandardResultsSetPagination

    def get(self, request, format=None):

        page_num = int(request.GET.get("page_num", 1))
        pizzas = FoodItem.objects.filter(item_type="pizza").order_by("id")
        paginator = Paginator(pizzas, app_settings.DEFAULT_PAGINATION_SIZE)
        if page_num > paginator.num_pages:
            return JsonResponse(
                {"success": False, "detail": "page_num exceeded limit"}
            )
        pizzas_page = paginator.page(page_num)
        serializer = PizzaSerializer(pizzas_page, many=True)
        return Response(serializer.data)


class ExtraList(APIView):
    def get(self, request):
        extras = FoodItem.objects.filter(item_type="extra").order_by("id")
        serializer = ExtraSerializer(extras, many=True)
        return Response(serializer.data)


class CreateOrder(APIView):
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            new_order = serializer.save()
            return JsonResponse(
                {"yo": str(serializer.validated_data), "order": str(new_order)}
            )
        return JsonResponse({"nope": serializer.errors})
