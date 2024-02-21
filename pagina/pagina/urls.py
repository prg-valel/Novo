from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', views.feed_page),
    path('publicate/', views.publicate_page),
    path('login/', views.login_page),
    path('signup/', views.signup_page),
    path('user/', views.user_page),
    path('logout/', views.logout_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)