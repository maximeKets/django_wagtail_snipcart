from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    subpage_types = [
        "home.Product",
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = Product.objects.live().descendant_of(self)
        return context


class Product(Page):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('price'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]

    @property
    def snipcart_details(self):
        """
        Formats product data for Snipcart.
        """
        return {
            "id": self.pk,
            "name": self.title,  # Using the Page model's title field for the product name
            "price": str(self.price),
            "description": self.description,
            "image": self.image if self.image else None,
            "url": self.full_url,  # Assuming full_url method returns the absolute URL of the product
        }

    def get_context(self, request, *args, **kwargs):
        """
        Adds snipcart_details to the context for use in templates.
        """
        context = super().get_context(request, *args, **kwargs)
        context['snipcart_details'] = self.snipcart_details
        return context
