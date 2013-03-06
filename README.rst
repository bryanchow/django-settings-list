django-settings-list
--------------------

A simple, reusable Django app that lists the settings values for a deployed or
running project using a custom admin view accessible only by superusers.

Technically, admin is not required, but by default the Settings List view is
styled similarly to Django Admin.


Installation
------------

1.  Make the `settings_list` module available in your Python environment.

2.  Make the ``settings_list/templates/`` directory available in your project,
    either by adding ``settings_list`` to ``INSTALLED_APPS`` and enabling the
    ``app_directories`` template loader, or by specifying the path manually in
    ``TEMPLATE_DIRS``.

3.  Add a URL pattern for the ``settings_list.views.settings_list`` view. For
    example::

        (r'^admin/settings/$', 'settings_list.views.settings_list'),


Keeping private settings private
--------------------------------

Django Settings List uses ``django.views.debug.get_safe_settings``, which
obfuscates "secret" settings (currently, any setting with a name containing
SECRET, PASSWORD, PROFANITIES_LIST, or SIGNATURE). This is the same filter
used by the debug traceback reporter.

You can also manually specify additional settings to keep private by adding a
PRIVATE_SETTINGS setting to your project. For example::

    PRIVATE_SETTINGS = [
        'AUTHNET_MERCHANT_ID',
        'AUTHNET_TRANSACTION_KEY',
        'AWS_ACCESS_KEY_ID',
        'AWS_SECRET_ACCESS_KEY',
    ]
