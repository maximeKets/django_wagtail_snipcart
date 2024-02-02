from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from django.db import models


@register_setting
class SnipcartSettings(BaseSiteSetting):
    api_key = models.CharField(
        max_length=255,
        help_text='Your Snipcart public API key'
    )
