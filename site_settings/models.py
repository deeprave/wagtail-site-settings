from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class ContactSettings(BaseSiteSetting):
    contact_button_text = models.CharField(
        null=True, blank=True, max_length=32, default="Form", help_text="Enter the text that will appear on the contact button"
    )
    contact_button_page = models.ForeignKey(
        "wagtailcore.Page",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Select the contact form page to link",
    )

    call_button_text = models.CharField(
        null=True, blank=True, max_length=32, default="Call", help_text="Enter the text that will appear on the call button"
    )
    call_button_number = models.CharField(null=True, blank=True, max_length=32, default=None, help_text="Enter the number to call")

    book_button_text = models.CharField(null=True, blank=True, max_length=32, help_text="Enter the text for make booking")
    book_button_link = models.URLField(null=True, blank=True, max_length=64, default=None, help_text="Enter the URL to make a booking")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("contact_button_text"),
                FieldPanel("contact_button_page"),
            ],
            heading="Contact Button",
        ),
        MultiFieldPanel(
            [
                FieldPanel("call_button_text"),
                FieldPanel("call_button_number"),
            ],
            heading="Call Button",
        ),
        MultiFieldPanel(
            [
                FieldPanel("book_button_text"),
                FieldPanel("book_button_link"),
            ],
            heading="Book Button",
        ),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_contact_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(blank=True, help_text="Enter your Facebook URL")
    linkedin = models.URLField(blank=True, help_text="Enter your LinkedIn URL")
    twitter = models.URLField(blank=True, help_text="Enter your Twitter URL")
    mastodon = models.URLField(blank=True, help_text="Enter your Mastodon URL")
    youtube = models.URLField(blank=True, help_text="Enter your YouTube URL")
    instagram = models.URLField(blank=True, help_text="Enter your Instagram URL")
    snapchat = models.URLField(blank=True, help_text="Enter your Snapchat URL")

    panels = [
        FieldPanel("facebook"),
        FieldPanel("linkedin"),
        FieldPanel("twitter"),
        FieldPanel("mastodon"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
        FieldPanel("snapchat"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_social_settings")
        cache.delete(key)
        return super().save(*args, **kwargs)
