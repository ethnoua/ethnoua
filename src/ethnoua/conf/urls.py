import os

from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.views.defaults import page_not_found

admin.autodiscover()
admin_media_dir = os.path.join(os.path.dirname(admin.__file__), 'media')


handler404 = lambda x: page_not_found(x, template_name='ethnoua/404.html')


def handler500(request):
    """
    500 error handler.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    context = {'request': request}

    t = loader.get_template('ethnoua/500.html')
    return HttpResponseServerError(t.render(Context(context)))

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
) 