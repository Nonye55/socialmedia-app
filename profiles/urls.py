from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view, \
    my_profile_update_view

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('update-profile', my_profile_update_view, name='my_profile_update_view'),
    path('my-invites/', invites_received_view, name='my_invites_view'),
    path('all-profiles/', profiles_list_view, name='all-profile-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profile-view'),

]
