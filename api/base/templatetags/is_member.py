from django import template
register = template.Library()

@register.simple_tag
def is_member(employee, members):
    for member in members:
        if employee.pk == member.pk:
            return 'checked'
    return ''