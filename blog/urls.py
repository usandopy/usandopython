
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views as sitemap_views
from main.sitemaps import StaticViewSitemap, TutorialViewSitemap, PostViewSitemap

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404


sitemaps = {
    'home-page': StaticViewSitemap,
    'tutorial': TutorialViewSitemap,
    'blog':  PostViewSitemap,
}


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', include('main.urls')),
    path('noticias/', include('mainsite.urls')),
    path('en/', include('main_en.urls')),
    path('es/', include('main_es.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('django_blog_it.urls')),
    path('blog_en/', include('django_blog_it_en.urls')),
    path('sitemaps.xml/', sitemap, {'sitemaps': sitemaps}),
    url(r'^accounts/', include('allauth.urls')),
    # This line for Django versions >=2.0
    #re_path('djga', include('google_analytics.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.error_404_view'

