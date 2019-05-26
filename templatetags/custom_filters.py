from django import template

register = template.Library()


@register.filter
def get_at_index(lis, index):
    return lis[index]
