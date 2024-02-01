from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def get_category_model_data():
    return Category.objects.all()
