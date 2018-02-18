from django.db import models


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % (self.semester_name)

    class Meta:
        ordering = ['semester_name']


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.course_number)

    class Meta:
        ordering = ['course_number']


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name']


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nickname)
        return result

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
        return '%s - %s (%s)' % (self.course.course_number, self.section_name, self.semester.semester_name)

    class Meta:
        ordering = ['course__course_number', 'section_name', 'semester__semester_name']





