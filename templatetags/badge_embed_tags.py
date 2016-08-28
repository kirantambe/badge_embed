from django import template

from badge_embed import WidgetStore
from django.template.base import Template
from django.template.context import Context
from django.utils.html import escape

register = template.Library()


def get_widget(name, **kwargs):
    """
    Fetches widget code from widgetstore, substites values recieved as kwargs in the widget code.
    returns the final code.
    """
    widget = WidgetStore.widgets.get(name, None)
    if not widget:
        raise Exception('Widget "{}" not registered or improperly registered'.format(name))
    final_code = Template(widget).render(Context(kwargs))
    return final_code


@register.simple_tag
def preivew_widget(name, **kwargs):
    return get_widget(name, **kwargs)


@register.simple_tag
def widget_code(name, **kwargs):
    return escape(get_widget(name, **kwargs))
