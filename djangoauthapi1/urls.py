from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls'))
]
