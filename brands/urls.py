from django.urls import path
from . import views


urlpatterns = [
    path('brands/list', views.BrandListView.as_view(), name='brand_list')
]
