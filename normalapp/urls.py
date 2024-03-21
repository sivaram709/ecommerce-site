from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.register,name="register"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("commerce",views.commerce,name="commerce"),
    path("signout",views.signout,name="signout"),
    path("feedback",views.feedback,name="feedback"),

]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)