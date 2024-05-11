from django.contrib import admin
from django.urls import path
from shop import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.ProductsListView.as_view(), name="products_list"),
    path("common/", v.product_list, name="product_list_common")
]
