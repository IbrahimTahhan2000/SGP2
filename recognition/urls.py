from django.urls import path
from . import views, views_al_fatiha, views_al_kawthar, views_al_fatiha_modefied, views_al_nas
from .views import user_login

## working well

# urlpatterns = [
#     # path('', views.home, name='home'),
#     # path("login/", user_login, name="login"),
#     path('login/', user_login, name='login'),  # ✅ Make login the first page
#     path('home/', views.home, name='home'),  # ✅ Redirect here after login
#
#     path('', views.welcome, name='welcome'),  # ✅ Welcome page (first page)
#     path('login/', views.user_login, name='login'),  # ✅ Login page
#     path('register/', views.register, name='register'),  # ✅ Registration page
#     path('home/', views.home, name='home'),  # ✅ Home page after login
#
#     # Surat Al-Fatiha URLs
#     path('surat_al_fatiha/', views_al_fatiha.surat_al_fatiha, name='surat_al_fatiha'),
#     # ✅ Surat Al-Fatiha with images
#     path('surat_al_fatiha_reading/', views.surat_al_fatiha_reading, name='surat_al_fatiha_reading'),
#
#     path('video_feed_al_fatiha/', views_al_fatiha.video_feed_al_fatiha, name='video_feed_al_fatiha'),
#     path('reset_sequences_al_fatiha/', views_al_fatiha.reset_sequences_al_fatiha, name='reset_sequences_al_fatiha'),
#     path('check_status_al_fatiha/', views_al_fatiha.check_sequence_status_al_fatiha, name='check_status_al_fatiha'),
#     path('current_sequence_status_al_fatiha/', views_al_fatiha.get_current_sequence_status_al_fatiha, name='current_sequence_status_al_fatiha'),
#
#     # Surat Al-Kawthar URLs
#     path('surat_al_kawthar/', views_al_kawthar.surat_al_kawthar, name='surat_al_kawthar'),
#
#     path('surat_al_kawthar_reading', views.surat_al_kawthar_reading, name='surat_al_kawthar_reading'),
#     # path('surat_al_kawthar_reading', views_al_kawthar.surat_al_kawthar_)
#     path('video_feed_al_kawthar/', views_al_kawthar.video_feed_al_kawthar, name='video_feed_al_kawthar'),
#     path('reset_sequences_al_kawthar/', views_al_kawthar.reset_sequences_al_kawthar, name='reset_sequences_al_kawthar'),
#     path('check_status_al_kawthar/', views_al_kawthar.check_sequence_status_al_kawthar, name='check_status_al_kawthar'),
#     path('current_sequence_status_al_kawthar/', views_al_kawthar.get_current_sequence_status_al_kawthar, name='current_sequence_status_al_kawthar'),
# ]

##

urlpatterns = [
    # path('', views.home, name='home'),
    # path("login/", user_login, name="login"),
    path('login/', user_login, name='login'),  # ✅ Make login the first page
    path('home/', views.home, name='home'),  # ✅ Redirect here after login

    path('', views.welcome, name='welcome'),  # ✅ Welcome page (first page)
    path('login/', views.user_login, name='login'),  # ✅ Login page
    path('register/', views.register, name='register'),  # ✅ Registration page
    path('home/', views.home, name='home'),  # ✅ Home page after login

    # Surat Al-Fatiha URLs
    path('surat_al_fatiha/', views_al_fatiha_modefied.surat_al_fatiha, name='surat_al_fatiha'),
    # ✅ Surat Al-Fatiha with images
    path('surat_al_fatiha_reading/', views.surat_al_fatiha_reading, name='surat_al_fatiha_reading'),

    path('video_feed_al_fatiha/', views_al_fatiha_modefied.video_feed_al_fatiha, name='video_feed_al_fatiha'),
    path('reset_sequences_al_fatiha/', views_al_fatiha_modefied.reset_sequences_al_fatiha, name='reset_sequences_al_fatiha'),
    path('check_status_al_fatiha/', views_al_fatiha_modefied.check_sequence_status_al_fatiha, name='check_status_al_fatiha'),
    path('current_sequence_status_al_fatiha/', views_al_fatiha_modefied.get_current_sequence_status_al_fatiha, name='current_sequence_status_al_fatiha'),

    # Surat Al-Kawthar URLs
    path('surat_al_kawthar/', views_al_kawthar.surat_al_kawthar, name='surat_al_kawthar'),

    path('surat_al_kawthar_reading', views.surat_al_kawthar_reading, name='surat_al_kawthar_reading'),
    # path('surat_al_kawthar_reading', views_al_kawthar.surat_al_kawthar_)
    path('video_feed_al_kawthar/', views_al_kawthar.video_feed_al_kawthar, name='video_feed_al_kawthar'),
    path('reset_sequences_al_kawthar/', views_al_kawthar.reset_sequences_al_kawthar, name='reset_sequences_al_kawthar'),
    path('check_status_al_kawthar/', views_al_kawthar.check_sequence_status_al_kawthar, name='check_status_al_kawthar'),
    path('current_sequence_status_al_kawthar/', views_al_kawthar.get_current_sequence_status_al_kawthar, name='current_sequence_status_al_kawthar'),

    path('surat_al_nas', views_al_nas.surat_al_fatiha, name='surat_al_nas'),
    path('surat_al_nas_reading', views.surat_al_nas_reading, name='surat_al_nas_reading'),
    path('video_feed_al_nas/', views_al_nas.video_feed_al_nas, name='video_feed_al_nas'),
    path('reset_sequences_al_nas/', views_al_nas.reset_sequences_al_nas, name='reset_sequences_al_nas'),
    path('check_status_al_nas/', views_al_nas.check_sequence_status_al_nas, name='check_status_al_nas'),
    path('current_sequence_status_al_nas/', views_al_nas.get_current_sequence_status_al_nas, name='current_sequence_status_al_nas'),

]
