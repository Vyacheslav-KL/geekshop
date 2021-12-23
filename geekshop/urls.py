from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

import mainapp.views as mainapp

urlpatterns = [
    re_path(r"^$", mainapp.main, name="main"),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^contact/", mainapp.contact, name="contact"),
    path("", include("social_django.urls", namespace="social")),
    re_path(r"^auth/", include("authnapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basketapp.urls", namespace="basket")),
    re_path(r"^order/", include("ordersapp.urls", namespace="order")),
    re_path(r"^admin/", include("adminapp.urls", namespace="admin")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
<<<<<<< HEAD
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
=======
    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
>>>>>>> a618191eb1b029e26c1bc97a38a86eab7bed6b2e
