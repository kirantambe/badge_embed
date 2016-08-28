from django.contrib.sites.shortcuts import get_current_site
from django.urls.base import reverse


class WidgetStore(object):
    """
    This class stores the html code that is needed which will call the widget
    Register new widgets using the register method
    """
    widgets = {
        'ExampleWidget': {
            'code': """<div id="ExampleWidget">
                        <script type="text/javascript" src="//{}/widget/?name={{name}}"></script>
                       </div>"""
        }
    }

    @staticmethod
    def register(name, widget_code):
        """
        Register a new widget by providing a name, and a dict containg 'code' as a key
        whose value should be set to the html code that is required to render the template.
        :param name: string
        :param widget_code: dict
        """
        WidgetStore.widgets[name] = widget_code
