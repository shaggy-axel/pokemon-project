from django.urls import path

from . import views


urlpatterns = [
    path('metrics/', views.CollectMetricView.as_view(), name='metrics')
]
