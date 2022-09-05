from django_hosts.defaults import host, patterns
from django.conf import settings

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, 'www'),
    host(r'api', 'Api.urls', 'api'),
    host(r'admin', 'GithubApiChart.admin_urls', 'admin'),
)