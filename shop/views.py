from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.


class ProductsListView(ListView):
    model = Product
    template_name = 'shop/products_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.GET.get('product_name')
        if product_name:
            queryset = queryset.filter(name__icontains=product_name)
        return queryset
    

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products_list.html', {'products': products})