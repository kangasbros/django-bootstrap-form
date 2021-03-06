from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(form):
    template = get_template("bootstrapform/form.html")
    context = Context({'form': form})
    return template.render(context)

@register.filter
def bootstrapfield(field):
    template = get_template("bootstrapform/field.html")
    context = Context({'field': field})
    return template.render(context)

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def is_datefield(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

