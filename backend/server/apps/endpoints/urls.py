# backend/server/apps/endpoints/urls.py file
#from django.conf.urls import url, include
from django.conf.urls import include
from django.urls import re_path
from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView


router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")


urlpatterns = [
    # url(r"^api/v1/", include(router.urls)),
    # re_path(r"^api/v1/", include(router.urls)),
     path("api/v1/", include(router.urls)),
    path(
        # "api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
        #'api/v1/income_classifier/predict', PredictView.as_view(), name='predict'
        'api/v1/<str:endpoint_name>/predict', PredictView.as_view(), name='predict'
    ),
]