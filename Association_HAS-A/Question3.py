
# Teacher And Course

class Teacher:
    def __init__(self,name,experience):
        self.name=name
        self.experience=experience

    def show_details(self,course):
        print(f"Teacher's Name : {self.name}")
        print(f"Experience : {self.experience}")
        print(f"Course Name : {course.course_name}")
        print(f"Duration : {course.duration}")

class Course:
    def __init__(self,course_name,duration):
        self.course_name=course_name
        self.duration=duration

teacher=Teacher("Rakesh Bhiaya","3 Years")
course=Course("Python","6 Month")

teacher.show_details(course)