from django.urls import path
from . views import api_manager_list_view, api_manager,api_manager_put,api_delete,api_manager_post

urlpatterns = [
    path('manager/', api_manager_list_view, name='list-managers'),
    path('manager/<int:id>/', api_manager, name='manager-details'),
    path('manager/<int:id>/update/', api_manager_put, name='update-manager'),
    path('manager/<int:id>/delete/', api_delete, name='delete-manager'),
    path('manager/<int:id>/post/',api_manager_post,name='post-manager')

]