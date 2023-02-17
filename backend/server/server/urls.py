"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# backend/server/server/urls.py file
# from django.conf.urls import url, include
# from django.conf.urls import include

# from django.urls import re_path
# from django.contrib import admin
# from django.urls import path

# from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

# from rest_framework.routers import DefaultRouter

# from apps.endpoints.views import EndpointViewSet
# from apps.endpoints.views import MLAlgorithmViewSet
# from apps.endpoints.views import MLRequestViewSet
# from apps.endpoints.views import PredictView # import PredictView



# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# urlpatterns += endpoints_urlpatterns


# #

# router = DefaultRouter(trailing_slash=False)
# router.register(r"endpoints", EndpointViewSet, basename="endpoints")
# router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
# router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

# urlpatterns = [
#     # url(r"^api/v1/", include(router.urls)),
#     path("api/v1/", include(router.urls)),
#     # add predict url
#     path(
#         # "api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
#         #'api/v1/income_classifier/predict', PredictView.as_view(), name='predict'
#         'api/v1/<str:endpoint_name>/predict', PredictView.as_view(), name='predict'
#     ),
# ]from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns
