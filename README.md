# wagtail-site-settings

Per site settings for contact and social media settings.

## Quick start


1. Add `site_settings` to your `INSTALLED_APPS` setting like this:
```python
    INSTALLED_APPS = [
        ...
        'site_settings',
    ]
```
2. Run `python manage.py migrate` to create the `site_settings` models.
3. `settings.site_settings.ContactSettings` and `settings.site_settings.SocialSettings` should now be available in templates globally.
