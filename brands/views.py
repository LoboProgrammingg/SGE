from django.views.generic import ListView
from . import models


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
