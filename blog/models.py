from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

# add this:
from wagtail.search import index

# Keep the definition of BlogIndexPage model, and add the BlogPage model:

class Category(ClusterableModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    body = RichTextField(blank=True)

    category = ParentalKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)

    @classmethod
    def get_category_model(self):
        return Category

    def main_image(self):
        gallery_item = self.image
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def get_absolute_url(self):
        return self.full_url

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('category'),
        FieldPanel('featured'),
    ]