from rest_framework import routers

from tasks.apps import TasksConfig
from tasks.views import ItemViewSet

app_name = TasksConfig.name

router = routers.DefaultRouter()
router.register(r"items", ItemViewSet, basename="item")

urlpatterns = []
urlpatterns += router.urls
