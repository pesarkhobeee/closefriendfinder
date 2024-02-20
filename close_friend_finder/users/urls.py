from django.urls import path

from close_friend_finder.users.views import user_detail_view
from close_friend_finder.users.views import user_redirect_view
from close_friend_finder.users.views import user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]
