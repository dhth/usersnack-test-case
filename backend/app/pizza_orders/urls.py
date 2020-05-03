from django.urls import path

from .views import (
    MovieList,
    MovieDetail,
    PizzaList,
    ExtraList,
    CreateOrder,
    OrderDetailView,
    OrderListView,
)


urlpatterns = [
    path("api/movies/", MovieList.as_view()),
    path("api/pizzas/", PizzaList.as_view()),
    path("api/extras/", ExtraList.as_view()),
    path("api/createorder/", CreateOrder.as_view()),
    path("api/orders/<int:pk>/", OrderDetailView.as_view()),
    path("api/orders/", OrderListView.as_view()),
    path("api/movies/<int:pk>/", MovieDetail.as_view()),
]
