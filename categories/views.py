from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
