from django.urls import path, include
from django.views import static
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:post_id>', views.single, name='single'),
    path('<slug:category>', views.archive, name='category')
]