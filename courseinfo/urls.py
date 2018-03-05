"""ez_university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from courseinfo.views import InstructorList, InstructorDetail, SectionList, SectionDetail, CourseList, CourseDetail, SemesterList, SemesterDetail, StudentList, StudentDetail


urlpatterns = [
    url(r'^instructor/$',
        InstructorList.as_view(),
        name='courseinfo_instructor_list_urlpattern'
        ),
    url(r'instructor/(?P<requested_instructor_id>[\d]+)/$',
        InstructorDetail.as_view(),
        name='courseinfo_instructor_detail_urlpattern'),

    url(r'^section/$',
        SectionList.as_view(),
        name='courseinfo_section_list_urlpattern'
        ),

    url(r'section/(?P<requested_section_id>[\d]+)/$',
        SectionDetail.as_view(),
        name='courseinfo_section_detail_urlpattern'),

    url(r'^course/$',
        CourseList.as_view(),
        name='courseinfo_course_list_urlpattern'
        ),
    url(r'course/(?P<requested_course_id>[\d]+)/$',
        CourseDetail.as_view(),
        name='courseinfo_course_detail_urlpattern'),

    url(r'^semester/$',
        SemesterList.as_view(),
        name='courseinfo_semester_list_urlpattern'
        ),
    url(r'semester/(?P<requested_semester_id>[\d]+)/$',
        SemesterDetail.as_view(),
        name='courseinfo_semester_detail_urlpattern'),

    url(r'^student/$',
        StudentList.as_view(),
        name='courseinfo_student_list_urlpattern'
        ),
    url(r'student/(?P<requested_student_id>[\d]+)/$',
        StudentDetail.as_view(),
        name='courseinfo_student_detail_urlpattern'),
]

