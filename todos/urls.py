from rest_framework import routers
from .views import TodoViewset
from django.urls import path


# urlpatterns = [
#     path('',TodoViewset.as_view(), name='todo')
# ]

router = routers.DefaultRouter()
router.register(r'api/todos',TodoViewset,'todos')
urlpatterns = router.urls