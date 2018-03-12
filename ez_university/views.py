from django.shortcuts import redirect


def redirect_root(request):
    return redirect('courseinfo_section_list_urlpattern')