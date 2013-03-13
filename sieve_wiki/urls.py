from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sieve_wiki.views.home', name='home'),
    # url(r'^sieve_wiki/', include('sieve_wiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern
urlpatterns += patterns('',
                        # Disabling account creation
                        (r"^_accounts/sign-up/$", "django.views.defaults.page_not_found"),
                        (r'^notify/', get_notify_pattern()),
                        (r'', get_wiki_pattern()),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
