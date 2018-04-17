from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import Context, loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm
from courseinfo.utils import PageLinksMixin
from .models import Instructor, Section, Course, Semester, Student


class InstructorList(PageLinksMixin,ListView):
    paginate_by=25
    model = Instructor



class InstructorDetail(View):
    def get(self, request, requested_instructor_id):
        instructor = get_object_or_404(
            Instructor,
            instructor_id=requested_instructor_id
        )
        section_list = instructor.sections.all()
        return render_to_response(
            'courseinfo/instructor_detail.html',
            {'instructor': instructor, 'section_list': section_list}
        )


class InstructorCreate(CreateView):
    form_class=InstructorForm
    model=Instructor


class InstructorUpdate(UpdateView):
    form_class=InstructorForm
    model=Instructor
    template_name='courseinfo/instructor_form_update.html'



class InstructorDelete(View):

    def get(self, request, requested_instructor_id):
        instructor = get_object_or_404(
            Instructor,
            instructor_id=requested_instructor_id
        )
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections, }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )

    def post(self, request, requested_instructor_id):
        instructor = get_object_or_404(
            Instructor,
            instructor_id=requested_instructor_id
        )
        instructor.delete()
        return redirect('courseinfo_instructor_list_urlpattern')


class SectionList(ListView):
    model = Section


class SectionDetail(View):
    def get(self, request, requested_section_id):
        section = get_object_or_404(
            Section,
            section_id=requested_section_id
        )
        semester = section.semester
        course = section.course
        instructor_list = section.instructors.all()
        student_list = section.students.all()
        return render_to_response(
            'courseinfo/section_detail.html',
            {'section': section,
             'semester': semester,
             'course': course,
             'instructor_list':instructor_list,
             'student_list':student_list}
        )


class SectionCreate(CreateView):
    form_class=SectionForm
    model=Section


class SectionUpdate(UpdateView):
    form_class=SectionForm
    model=Section
    template_name='courseinfo/section_form_update.html'

class SectionDelete(DeleteView):
    model = Section
    success_url=reverse_lazy('courseinfo_section_list_urlpatter')



class CourseList(ListView):
    model = Course


class CourseDetail(View):
    def get(self, request, requested_course_id):
        course = get_object_or_404(
            Course,
            course_id=requested_course_id
        )
        section_list=course.sections.all()
        return render_to_response(
            'courseinfo/course_detail.html',
            {'course':course, 'section_list': section_list}
        )


class CourseCreate(CreateView):
    form_class=CourseForm
    model=Course


class CourseUpdate(UpdateView):
    form_class=CourseForm
    model=Course
    template_name='courseinfo/course_form_update.html'


class CourseDelete(View):

    def get(self, request, requested_course_id):
        course = get_object_or_404(
            Course,
            course_id=requested_course_id
        )
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections, }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )

    def post(self, request, requested_course_id):
        course = get_object_or_404(
            Course,
            course_id=requested_course_id
        )
        course.delete()
        return redirect('courseinfo_course_list_urlpattern')


class SemesterList(ListView):
    model = Semester

class SemesterDetail(View):
    def get(self, request, requested_semester_id):
        semester = get_object_or_404(
            Semester,
            semester_id=requested_semester_id
        )
        section_list = semester.sections.all()
        return render_to_response(
            'courseinfo/semester_detail.html',
            {'semester': semester, 'section_list': section_list}
        )


class SemesterCreate(CreateView):
    form_class=SemesterForm
    model=Semester



class SemesterUpdate(UpdateView):
    form_class=SemesterForm
    model=Semester
    template_name='courseinfo/semester_form_update.html'

class SemesterDelete(View):

    def get(self, request, requested_semester_id):
        semester = get_object_or_404(
            Semester,
            semester_id=requested_semester_id
        )
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections, }
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )

    def post(self, request, requested_semester_id):
        semester = get_object_or_404(
            Semester,
            semester_id=requested_semester_id
        )
        semester.delete()
        return redirect('courseinfo_semester_list_urlpattern')


class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Student


class StudentDetail(View):
    def get(self, request, requested_student_id):
        student = get_object_or_404(
            Student,
            student_id=requested_student_id
        )
        section_list = student.sections.all()
        return render_to_response(
            'courseinfo/student_detail.html',
            {'student': student, 'section_list': section_list}
        )


class StudentCreate(CreateView):
    form_class=StudentForm
    model=Student



class StudentUpdate(UpdateView):
    form_class=StudentForm
    model=Student
    template_name='courseinfo/student_form_update.html'


class StudentDelete(View):

    def get(self, request, requested_student_id):
        student = get_object_or_404(
            Student,
            student_id=requested_student_id
        )
        sections = student.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'sections': sections, }
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )

    def post(self, request, requested_student_id):
        student = get_object_or_404(
            Student,
            student_id=requested_student_id
        )
        student.delete()
        return redirect('courseinfo_student_list_urlpattern')




