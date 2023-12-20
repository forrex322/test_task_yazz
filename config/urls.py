from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from graphene_django.views import GraphQLView


# Swagger configs
schema_view = get_schema_view(
    openapi.Info(
        title=settings.ADMIN_SITE_TITLE,
        default_version="v1",
    ),
    validators=[],
    public=True,
    permission_classes=(AllowAny,),
    authentication_classes=(),
)

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    re_path("health-check/$", lambda request: HttpResponse(status=200)),
    # drf-yasg url
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # API urls
    path(
        "api/v1/",
        include(
            (
                [
                    path("", include(("users.urls", "users"))),
                    path("", include(("files.urls", "files"))),
                    path("graphql", GraphQLView.as_view(graphiql=True)),
                ],
                "api",
            ),
            namespace="api",
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

# Admin Site Config
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#adminsite-attributes
admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
