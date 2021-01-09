'''
Introduction
Given a diagram, determine which plants each child in the kindergarten class is responsible for.

The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, 
plant them in actual dirt, and grow actual plants.

They've chosen to grow grass, clover, radishes, and violets.

To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, 
choosing randomly from the available types of seeds.

[window][window][window]
........................ # each dot represents a cup
........................
There are 12 children in the class:

Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.

The following diagram represents Alice's plants:

[window][window][window]
VR......................
RG......................
In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.

Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, 
it should be able to determine which plants belong to each student.

For example, if it's told that the garden looks like so:

[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
Then if asked for Alice's plants, it should provide:

Violets, radishes, violets, radishes
While asking for Bob's plants would yield:

Clover, grass, clover, clover
'''

class Garden:
    
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 
                                        'Eve', 'Fred', 'Ginny', 'Harriet', 
                                        'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram.splitlines()
        if len(self.diagram) > 2:
            raise Exception("Garden can only fit two rows!")

        for l in self.diagram:
            if len(l) > 24:
                raise Exception("Garden can only fit 24 pots in a row!")

        # Also validate that only 'R/C/G/V are used?!
        # pass

        # alphabetize students
        self.students = sorted(students)
        # grass, clover, radishes, and violets
        self.plant_names = { 'R': 'Radishes', 'C' : 'Clover', 'G': 'Grass', 'V': 'Violets' }

    def plants(self, student):
        studentrowoffset = self.students.index(student) * 2
        # I am not too happy with the slicing syntax... will look at better solutions
        studentsplants = self.diagram[0][studentrowoffset:studentrowoffset+2:1] + self.diagram[1][studentrowoffset:studentrowoffset+2:1]
        plants = []
        for plantinitial in studentsplants:
            plants.append(self.get_plant_names(plantinitial))

        return plants

    def get_plant_names(self, plant_name):
        return self.plant_names[plant_name]


# Test code
# garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
# print(garden.plants("Alice")) # ["Radishes", "Clover", "Grass", "Grass"]
# garden = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
# print(garden.plants("Xander"))

# Exceptions:
# garden = Garden("RC\nVRCGVVRVCGGCCGVRGCVCGCGVGV") # Too many in a row
# garden = Garden("RC\nGG\nGG") # Too many rows