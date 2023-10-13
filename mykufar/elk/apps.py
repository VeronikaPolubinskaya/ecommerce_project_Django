from django.apps import AppConfig


class ElkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elk'
    elasticsearch_dsl_options = {'http_auth': ('elastic', 'MyPw123')}


# from django_elasticsearch_dsl.drf.indices import AppConfig
#
# class MyAppConfig(AppConfig):
