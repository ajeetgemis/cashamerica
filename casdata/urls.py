from django.contrib import admin
from django.urls import path,include
from casdata import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup_view),
    path('signup',views.signup_view,name="signup"),
    path('verify',views.verify,name="verify"),
    path('signin',views.index,name='signin'),
    path('tata_api/',views.exposedata.as_view(),name="tata_api"),
]
