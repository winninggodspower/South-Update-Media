from django.shortcuts import render, get_object_or_404
from .models import Category, BlogPage

# Create your views here.
def category_view(requests, slug):
    category_model = get_object_or_404(Category, slug=slug)

    context = {
        "page": BlogPage.objects.filter(category=category_model),
        "category": category_model.name
    }

    return render(requests, 'category.html', context)