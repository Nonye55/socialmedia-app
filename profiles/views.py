from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm
# from django.views.generic import ListView


# Create your views here.

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/myprofile.html', context)


def my_profile_update_view(request):
    # print(request.user)
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    print(profile)
    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,

    }
    print(profile)
    return render(request, 'profiles/update-profile.html', context)


def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)

    context = {'qs': qs}
    return render(request, 'profiles/my-invites.html', context)


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {'qs': qs}
    return render(request, 'profiles/profile_list.html')


def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {'qs': qs}
    return render(request, 'profiles/to_invite_list.html')
