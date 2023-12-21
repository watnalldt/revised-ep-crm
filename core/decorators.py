from django.urls import reverse
from django.utils.html import format_html


def admin_changelist_url(model):
    app_label = model._meta.app_label
    model_name = model.__name__.lower()
    return reverse(f"admin:{app_label}_{model_name}_changelist")


def admin_changelist_link(attr, short_description, empty_description="-", query_string=None):
    def wrap(func):
        def field_func(self, obj):
            related_obj = getattr(obj, attr)
            if related_obj is None:
                return empty_description
            url = admin_changelist_url(related_obj.model)
            if query_string:
                url += "?" + query_string(obj)
            return format_html('<a href="{}">{}</a>', url, func(self, related_obj))

        field_func.short_description = short_description
        field_func.allow_tags = True
        return field_func

    return wrap
