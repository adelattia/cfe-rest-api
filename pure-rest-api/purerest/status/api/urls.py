from django.conf.urls import url
# from .views import StatusListSearchAPIView
from .views import StatusAPIView, StatusAPIDetailView


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'(?P<pk>\d+)/$', StatusAPIDetailView.as_view()),
]