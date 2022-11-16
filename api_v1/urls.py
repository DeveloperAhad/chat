from django.urls import path, include

from api_v1.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('rest-auth/', include('rest_framework.urls')),
]