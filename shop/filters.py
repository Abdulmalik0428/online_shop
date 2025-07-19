# filters.py
import django_filters
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Kategoriya bo‘yicha",
        empty_label="Barchasi"
    )

    class Meta:
        model = Product
        fields = ['category']


