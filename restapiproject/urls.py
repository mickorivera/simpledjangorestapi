from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^api/v1/', include('restapiapp.urls')),
    url(r'^api/auth/token/$', obtain_jwt_token),
]