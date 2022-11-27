
from contextlib import _RedirectStream
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="RentHome"),
    path("about", views.about,name="AboutUs"),
    path('contact', views.contact,name="ContactUs"),
    path('owner', views.owner,name="owner"),
    path('tenant', views.tenant,name="tenant"),
    path('signup', include('authentication.urls'),name="signup"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('saveAdd', views.saveAdd, name="saveAdd"),
    path('houseDetails/<str:id>',views.houseDetails,name="houseDetails")
] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)