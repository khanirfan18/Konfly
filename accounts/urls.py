from django.urls import path,include
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/",views.HandleNewUser.as_view(),name="signup"),
    path("login/",views.HandleOldUser.as_view(),name="login"),
    # path("profile/",views.index,name="profile"),

]

