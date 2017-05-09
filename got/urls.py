from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from houses.views import MajorHouseListView, HouseDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MajorHouseListView.as_view(), name="major_house_list_view"),
    url(r'^house/(?P<pk>\d+)$', HouseDetailView.as_view(), name='house_detail_view' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
