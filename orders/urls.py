from django.urls import path

from .views import checkout, order_summary

urlpatterns = [
    path("", checkout, name="checkout"),
    path("summary/<int:order_id>/", order_summary, name="order_summary"),
]
