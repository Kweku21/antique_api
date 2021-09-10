from django.urls import path

from users.views import LoginView, UserAutoBidConfigView

urlpatterns = [
    path('login/', LoginView.as_view(http_method_names=['post']), name="login"),
    path('auto-bid/configure/', UserAutoBidConfigView.as_view(http_method_names=['post']), name="auto-bid-config"),
]
