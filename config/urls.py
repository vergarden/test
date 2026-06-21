from django.contrib import admin
from django.urls import path
from core.views import api_root, boardsaying_list, boardsaying_count, emailsending_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/boardsaying/', boardsaying_list, name='boardsaying-list'),
    path('api/boardsaying/count/', boardsaying_count, name='boardsaying-count'),
    path('api/emailsending/', emailsending_create, name='emailsending-create'),
]
