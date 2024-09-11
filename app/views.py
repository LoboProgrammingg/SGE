from django.shortcuts import render
from . import metrics


def home(request):
    product_metrics = metrics.get_product_metrics()

    context = {
        'product_metrics': product_metrics
    }
    return render(request, 'home.html', context)