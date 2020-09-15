from django.template.defaulttags import register

@register.filter
def get_item(data, key):
    return data.get(key)