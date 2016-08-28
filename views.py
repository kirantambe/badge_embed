from django.conf import settings
from django.template import Template
from django.template.context import Context
from django.http.response import HttpResponse
from django.views.generic.detail import BaseDetailView
from django.contrib.sites.shortcuts import get_current_site


class BaseWidgetView(BaseDetailView):
    loader_js = None
    model = None

    def render_to_response(self, context, **response_kwargs):
        if not self.__class__.loader_js:
            raise Exception('loader_js cannot be None.')
        js_file_template = None
        with open(self.__class__.loader_js) as js_file:
            js_file_template = Template(js_file.read())
        context['static_files'] = '//{}{}'.format(get_current_site(self.request).domain, settings.STATIC_URL)
        context.update(self.request.GET.dict())
        rendered_js = js_file_template.render(Context(context))
        return HttpResponse(rendered_js, content_type='application/javascript')


