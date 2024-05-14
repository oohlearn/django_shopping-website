from django.contrib import admin
from django.urls import path
from shop import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.ProductsListView.as_view(), name="products_list"),
    path("common/", v.product_list, name="product_list_common"),
    path("<int:pk>/", v.ProductDetailView.as_view(), name="product_detail"),
    path("common/<int:id>", v.product_detail, name="detail_common"),
    path("checkout/", v.checkout, name="checkout"),
    path("success/", v.success_order, name="success")
]
