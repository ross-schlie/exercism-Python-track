"""exercism kindergarten garden module."""


class Garden:

    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David',
                                        'Eve', 'Fred', 'Ginny', 'Harriet',
                                        'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        """Create a Garden and keep a diagram of students plants."""
        self.diagram = diagram.splitlines()
        if len(self.diagram) > 2:
            raise Exception("Garden can only fit two rows!")

        for l in self.diagram:
            if len(l) > 24:
                raise Exception("Garden can only fit 24 pots in a row!")

        # Also validate that only 'R/C/G/V are used?

        self._students = sorted(students)
        self._plant_names = {'R': 'Radishes',
                            'C': 'Clover',
                            'G': 'Grass',
                            'V': 'Violets'}

    def plants(self, student):
        """Find the plants of a given student."""
        offset = self._students.index(student) * 2
        studentsplants = self.diagram[0][offset:offset+2:1] \
                        + self.diagram[1][offset:offset+2:1]
        plants = []
        for plantinitial in studentsplants:
            plants.append(self._plant_name(plantinitial))

        return plants
        # Much nicer solution as per vianney-g
        # return [self._plant_names(p[i])
        #   for p in self.diagram
        #       for i in (studentrowoffset, studentrowoffset + 1)]

    def _plant_name(self, plant_name):
        """Get the name of a given plant."""
        return self._plant_names[plant_name]

