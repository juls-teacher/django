"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from products.views import index, products, add_product, details
from profiles.views import profiles, register, login_view, logout_view
from notes.views import notes, add_notes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.url", namespace="api")),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("profiles/", profiles, name="profiles"),
    path("products/", products, name="products"),
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("add_product/", add_product, name="add_product"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("notes/", notes, name="notes"),
    path("add_notes/", add_notes, name="add_notes"),
    path("details/<int:product_id>/", details, name="details"),
    # path("cart/", cart, name="cart"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
