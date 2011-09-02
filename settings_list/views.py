from django.conf import settings
from django.views.debug import get_safe_settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response


PRIVATE_SETTINGS = getattr(settings, 'PRIVATE_SETTINGS', [])


@staff_member_required
def settings_list(request):
    """
    Custom admin view that displays the settings for this Django project.
    """

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))

    settings = get_safe_settings()

    for setting in PRIVATE_SETTINGS:
        if setting in settings:
            settings[setting] = '********************'

    sorted_settings = sorted(settings.items())

    return render_to_response('admin/settings_list.html', RequestContext(request, {
        'title': 'Django Settings',
        'sorted_settings': sorted_settings,
    }))
