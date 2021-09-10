from django.urls import path

from users.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(http_method_names=['post']), name="login"),
]