from django.conf import settings
from django.views.debug import get_safe_settings
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.shortcuts import render_to_response


PRIVATE_SETTINGS = getattr(settings, 'PRIVATE_SETTINGS', [])


@staff_member_required
def settings_list(request):
    """
    Custom admin view that displays the settings for this Django project.
    """

    settings = get_safe_settings()

    for setting in PRIVATE_SETTINGS:
        if setting in settings:
            settings[setting] = '********************'

    return render_to_response('admin/settings_list.html', RequestContext(request, {
        'settings': settings,
    }))
