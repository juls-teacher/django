from django.urls import include, path
from rest_framework import routers

from api.products.views import ProductViewSet
from api.notes.views import NoteViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"notes", NoteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


