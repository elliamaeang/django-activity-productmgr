from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path("",views.index,name="index"),
    path("add/", views.add, name="add"),
    path("update/<int:product_id>", views.update),
    path("delete/<int:product_id>", views.delete)
]