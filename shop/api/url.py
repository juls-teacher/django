from django.urls import include, path
from rest_framework import routers

from api.products.views import ProductViewSet, TheMostExpensiveProductSet, TheMostPopularProductSet
from api.notes.views import NoteViewSet
from api.users.views import RegisterView, LoginView

app_name = "api"

router = routers.DefaultRouter()

router.register(r"products", ProductViewSet)
router.register(r"notes", NoteViewSet)

urlpatterns = [

    path('products/expensive/', TheMostExpensiveProductSet.as_view(), name="products_expensive"),
    path('products/popular/', TheMostPopularProductSet.as_view(), name="products_popular"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path("", include(router.urls)),
    # path('logout/', LogoutView.as_view(), name='logout'),

]


