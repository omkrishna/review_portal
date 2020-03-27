
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from review import views as review_views
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('review.urls')),
    path('course/<id>/', review_views.course_detail, name = 'course_detail'),
    path('prof/<id>/', review_views.prof_detail, name = 'prof_detail'),
    path('register/',user_views.register, name='register'),
    path('profile_home/',user_views.profile_home, name='profile_home'),
    path('profile_update/',user_views.profile_update, name='profile_update'),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)