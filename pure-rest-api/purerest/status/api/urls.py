from django.conf.urls import url
# from .views import StatusListSearchAPIView
from .views import (
    StatusAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
)


urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'(?P<pk>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]


# 1

# /api/status/ -> list
# /api/status/create/ -> create
# /api/status/id/ -> detail
# /api/status/id/update -> update
# /api/status/id/delete -> delete


# 2
# /api/status/ -> list
# /api/status/id/ -> crud


#3
# /api/status/ -> crud and list/search