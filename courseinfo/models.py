from django.db import models
from django.core.urlresolvers import reverse


class CalendarPeriod(models.Model):
    calendar_period_id = models.IntegerField(primary_key=True)
    calendar_period_name = models.CharField(max_length=45,unique=True)

    def __str__(self):
        return '%s' % (self.calendar_period_name)

    class Meta:
        ordering = ['calendar_period_id']


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    # semester_name = models.CharField(max_length=45, unique=True)  deleted field
    year = models.IntegerField()    # added field
    calendar_period = models.ForeignKey(CalendarPeriod, related_name='semesters')  # added field

    def __str__(self):
        # return '%s' % (self.semester_name)   old version
        return '%s - %s' % (self.year, self.calendar_period.calendar_period_name)   # new version

    def get_absolute_url(self):
        return reverse('courseinfo_semester_detail_urlpattern',
                kwargs={'requested_semester_id': self.semester_id}
                )

    def get_update_url(self):
        return reverse('courseinfo_semester_update_urlpattern',
                       kwargs={'pk': self.semester_id}
        )

    def get_delete_url(self):
        return reverse(
            'courseinfo_semester_delete_urlpattern',
            kwargs={'requested_semester_id': self.semester_id}
        )

    class Meta:
        # ordering = ['semester_name']  old version
        ordering = ['year', 'calendar_period__calendar_period_id'] # revised version
        unique_together = ('year', 'calendar_period')  # added



class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.course_number)

    def get_absolute_url(self):
        return reverse('courseinfo_course_detail_urlpattern',
                kwargs={'requested_course_id': self.course_id}
                )

    def get_update_url(self):
        return reverse('courseinfo_course_update_urlpattern',
                       kwargs={'pk': self.course_id}
        )

    def get_delete_url(self):
        return reverse(
            'courseinfo_course_delete_urlpattern',
            kwargs={'requested_course_id': self.course_id}
        )

    class Meta:
        ordering = ['course_number']


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name )

    def get_absolute_url(self):
        return reverse('courseinfo_instructor_detail_urlpattern',
                kwargs={'requested_instructor_id': self.instructor_id}
                )

    def get_update_url(self):
        return reverse('courseinfo_instructor_update_urlpattern',
                       kwargs={'pk': self.instructor_id}
        )

    def get_delete_url(self):
        return reverse(
            'courseinfo_instructor_delete_urlpattern',
            kwargs={'requested_instructor_id': self.instructor_id}
        )

    class Meta:
        ordering = ['last_name', 'first_name']


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name )
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nickname )
        return result

    def get_absolute_url(self):
        return reverse('courseinfo_student_detail_urlpattern',
                kwargs={'requested_student_id': self.student_id}
                )

    def get_update_url(self):
        return reverse('courseinfo_student_update_urlpattern',
                       kwargs={'pk': self.student_id}
        )

    def get_delete_url(self):
        return reverse(
            'courseinfo_student_delete_urlpattern',
            kwargs={'requested_student_id': self.student_id}
        )

    class Meta:
        ordering = ['last_name', 'first_name']


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, related_name='sections')
    course = models.ForeignKey(Course, related_name='sections')
    instructors = models.ManyToManyField(Instructor, related_name='sections')
    students = models.ManyToManyField(Student, related_name='sections')

    def __str__(self):
        # return '%s - %s (%s)' % (self.course.course_number, self.section_name, self.semester.semester_name)
        return '%s - %s (%s)' % (self.course.course_number, self.section_name, self.semester.__str__())

    def get_absolute_url(self):
        return reverse('courseinfo_section_detail_urlpattern',
                kwargs={'requested_section_id': self.section_id}
                )

    def get_update_url(self):
        return reverse('courseinfo_section_update_urlpattern',
                       kwargs={'pk': self.section_id}
        )

    def get_delete_url(self):
        return reverse(
            'courseinfo_section_delete_urlpattern',
            kwargs={'pk': self.section_id}
        )

    class Meta:
        # ordering = ['course__course_number', 'section_name', 'semester__semester_name']
        ordering = ['course__course_number', 'section_name', 'semester']
