from django.contrib import admin
from django.urls import path, include
from .views import show_main
from .views import show_main, create_product
from main.views import show_main, create_product, show_xml 
from main.views import show_main, create_product, show_xml, show_json
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register_user
from main.views import login_user 
from main.views import logout_user
from django.urls import path
from . import views  # Import your views module here


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),  # Define a URL pattern for the show_main view
    path('admin/', admin.site.urls),
    path('create-product', create_product, name='create_product'),
    path('add_sub_item/<int:id>/<int:option>/', views.add_sub_item, name='add_sub_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register_user, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout')

]
