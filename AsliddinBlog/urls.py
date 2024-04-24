from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', HomeView.as_view(), name='home'),
  path('blog/', BlogView.as_view(), name='blog'),
  path('blog/<int:pk>/maqola', MaqolaView.as_view(), name='maqola'),
  path('talks/', TalkView.as_view(), name='talks'),
  path('about/', AboutView.as_view(), name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
