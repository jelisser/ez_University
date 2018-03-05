from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Context, loader
from django.views import View

from .models import Instructor, Section, Course, Semester, Student


class InstructorList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list':Instructor.objects.all()}
        )


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


class SectionList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list':Section.objects.all()}
        )


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


class CourseList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list':Course.objects.all()}
        )


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


class SemesterList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'semester_list':Semester.objects.all()}
        )

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


class StudentList(View):
    def get(self,request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'student_list':Student.objects.all()}
        )


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




