"""
create first page
1.* ver > url function 정규식 구성(가독성 하락)
2.0 ~ > path function
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
