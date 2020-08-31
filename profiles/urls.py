from django.urls import path

from .views import my_profile_view, invites_received_view, invite_profiles_list_view, ProfileDetailView, \
    my_profile_update_view, ProfileListView, send_invitation, remove_from_friends, accept_invitation, reject_invitation

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('update-profile', my_profile_update_view, name='my_profile_update_view'),
    path('my-invites/', invites_received_view, name='my_invites_view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profile-view'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    # path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject_invite')

]
