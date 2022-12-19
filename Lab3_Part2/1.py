from abc import ABC, abstractmethod


class ICourse(ABC):

    amount_teachers = 0

    @abstractmethod
    def __init__(self, course, teachers):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, name):
        if not isinstance(name, str):
            raise TypeError("Course must be string")
        self.__course = name

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        for i in teachers:
            if not isinstance(i, ITeacher):
                raise TypeError("Teacher must be ITeacher")
            self.amount_teachers += 1
        self.__teachers = teachers

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.amount_teachers:
            self.index += 1
            return self.__teachers[self.index - 1]
        raise StopIteration


class ILocalCourse(ICourse):

    @abstractmethod
    def __init__(self, course, teachers, lab):
        pass

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, number):
        if not isinstance(number, int):
            raise TypeError("Laboratory number must be int")
        self.__lab = number


class IOffsiteCourse(ICourse):

    @abstractmethod
    def __init__(self, course, teachers, loc):
        pass

    @property
    def loc(self):
        return self.loc

    @loc.setter
    def loc(self, location):
        if not isinstance(location, str):
            raise TypeError("Location must be str")
        self.__loc = location


class ITeacher:
    @abstractmethod
    def __init__(self, name, knowledge, years_of_work):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, line):
        if not isinstance(line, str):
            raise TypeError("Name must be string")
        self.__name = line

    @property
    def knowledge(self):
        return self.__knowledge

    @knowledge.setter
    def knowledge(self, line):
        if not isinstance(line, str):
            raise TypeError("Knowledge must be string")
        self.__knowledge = line

    @property
    def years_of_work(self):
        return self.__years_of_work

    @years_of_work.setter
    def years_of_work(self, line):
        if not isinstance(line, int):
            raise TypeError("Years of work must be integer")
        self.__years_of_work = line


class ICourseFactory(ABC):

    @abstractmethod
    def teacher(self, name, knowledge, years_of_work) -> ITeacher:
        pass

    @abstractmethod
    def local_course(self, course, teachers, lab) -> ILocalCourse:
        pass

    @abstractmethod
    def offsite_course(self, course, teachers, loc) -> IOffsiteCourse:
        pass


class LocalCourse(ILocalCourse):

    def __init__(self, course, teachers, lab):
        self.course = course
        self.teachers = teachers
        self.lab = lab

    def __str__(self):
        it = iter(self)
        a = ''
        while True:
            try:
                a += f'{next(it)}'
            except StopIteration:
                break
        return f'{self.course} | {a} | {self.lab}\n'

    def __add__(self, other):
        if not isinstance(other, ITeacher):
            raise TypeError("Teacher must have type ITeacher")

        self.teachers.append(other)

        return LocalCourse(self.course, self.teachers, self.lab)

    def __sub__(self, other):
        if not isinstance(other, ITeacher):
            raise TypeError("Teacher must have type ITeacher")
        self.teachers.remove(other)
        return LocalCourse(self.course, self.teachers, self.lab)


class OffsiteCourse(IOffsiteCourse):

    def __init__(self, course, teachers, loc):
        self.course = course
        self.teachers = teachers
        self.loc = loc

    def __str__(self):
        return f'{self.course} | {self.teachers} | {self.loc}\n'


class Teacher(ITeacher):
    def __init__(self, name, knowledge, years_of_work=int):
        self.name = name
        self.knowledge = knowledge
        self.years_of_work = years_of_work

    def __str__(self):
        return f"{self.name}, {self.knowledge}, {self.years_of_work}. "


class CourseFactory(ICourseFactory):

     def teacher(self, name, knowledge, years_of_work) -> ITeacher:
         return Teacher(name, knowledge, years_of_work)

     def local_course(self, course, teachers, lab) -> ILocalCourse:
         return LocalCourse(course, teachers, lab)

     def offsite_course(self, course, teachers, loc) -> IOffsiteCourse:
         return OffsiteCourse(course, teachers, loc)


blabla = CourseFactory()


a = blabla.teacher("John Johns", "Maths", 10)
b = blabla.teacher("Anna Ananas", "Physics", 7)
c = blabla.teacher("Beck Beckman", "Biology", 5)
d = blabla.teacher("Walter White", "Chemistry", 15)
e = blabla.teacher("Oscar Oscars", "Singing", 9)

x1 = blabla.local_course("aaaaaa", [a, b, e], 1)

print(x1)

x1 = x1-a

print(x1)

x1 = x1+c

print(x1)

x1 = x1 - e
x1 = x1 + d

print(x1)
