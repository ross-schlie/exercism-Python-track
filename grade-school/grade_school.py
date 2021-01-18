class School:

    MAX_GRADE = 8

    def __init__(self):
        """A school that maintains an internal database of studens per grade."""
        self._db = {}
        for i in range(1, self.MAX_GRADE):
            self._db[i] = []

    def add_student(self, name, grade):
        """Add a student at a given grade to the schoolds database."""
        self._db[grade].append(name)

    def roster(self):
        """Get a list of all school students.
        
        The list is ordered by grade, with students in a grade alphabetized
            as per grade(grade_number)
        """
        allstudents = []
        for grade_number in range(1, self.MAX_GRADE):
            allstudents.extend(self.grade(grade_number))

        return allstudents

    def grade(self, grade_number):
        """Get a list of all students in a specified grade (alphabetized)."""
        return sorted(self._db[grade_number])

    def db(self):
        return self._db.copy()