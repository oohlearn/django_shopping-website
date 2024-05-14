from django.shortcuts import render
from .models import Product, Order
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

# Create your views here.


class ProductsListView(ListView):
    model = Product
    template_name = 'shop/products_list.html'
    context_object_name = 'products'
    paginate_by = 4

    # search for products
    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.GET.get('product_name')
        if product_name:
            queryset = queryset.filter(name__icontains=product_name)
        return queryset
    

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products_list.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get("items", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zipcode = request.POST.get("zipcode", "")
        total = request.POST.get("total", "")

        order = Order(items=items, name=name, email=email, address=address,
                      city=city, state=state, zipcode=zipcode, total=total)

        order.save()

    return render(request, 'shop/checkout.html')


def success_order(request):
    return render(request, 'shop/success_order.html')
