from django.urls import path

from .views import (
    CreateOrder,
    ExtraList,
    OrderDetailView,
    OrderListView,
    PizzaList,
)

urlpatterns = [
    path("api/pizzas/", PizzaList.as_view()),
    path("api/extras/", ExtraList.as_view()),
    path("api/createorder/", CreateOrder.as_view()),
    path("api/orders/<int:pk>/", OrderDetailView.as_view()),
    path("api/orders/", OrderListView.as_view()),
]
