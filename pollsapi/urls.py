from django.urls import include, path
from .views import polls_detail, polls_list
from rest_framework.compat import re_path
# from .apiviews import PollList, PollDetail which should not be imported when using ViewSet
from pollsapi.apiviews import ChoiceList, CreateVote, LoginView, UserCreate
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet


router = DefaultRouter()
router.register(r'pollsapi/', PollViewSet, basename='pollsapi')

# urlpatterns = [
#     # re_path(r'^', include('pollsapi.urls'))
# ]
# to obtain a login endpoint, we can use obtain_auth_token of DRF by importing views of DRF
urlpatterns = [
    # path("pollsapi/", PollList.as_view(), name="polls_list"),
    # path("pollsapi/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("user/", UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls

# Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
# Use generics.* when you only want to allow some operations on a model
# Use APIView when you want to completely customize the behaviour.