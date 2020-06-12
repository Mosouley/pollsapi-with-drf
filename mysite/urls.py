from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path
# from pollsapi.apiviews import PollViewSet



urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('pollsapi/', include('pollsapi.urls')),
]


# urlpatterns += router.urls
# urlpatterns += [
#     path('pollsapi/', include('pollsapi.urls')),
# ]
