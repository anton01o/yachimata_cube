from yachimata_cube import *
import pickle

bp1 = [[0,1,0,0],
       [1,1,1,0],
       [1,1,1,1]]
bp2 = [[1,1,1,1],
       [0,0,0,1],
       [0,1,1,1]]
bp3 = [[0,1,1,0],
       [1,1,0,0],
       [1,1,1,1]]
bp4 = [[1,0,0,0],
       [1,1,0,1],
       [1,1,1,1]]
bp5 = [[0,0,1,1],
       [1,0,0,1],
       [1,1,1,1]]
bp6 = [[0,0,0,1],
       [1,1,0,1],
       [1,1,1,1]]
bp7 = [[1,1,0,0],
       [1,1,0,0],
       [1,1,1,1]]
bp8 = [[0,0,0,0],
       [1,1,1,1],
       [1,1,1,1]]

element1 = YachiElement(bp1,1,[1,1,1])
element2 = YachiElement(bp2,2,[1,1,1])
element3 = YachiElement(bp3,3,[1,1,1])
element4 = YachiElement(bp4,4,[1,1,1])
element5 = YachiElement(bp5,5,[1,1,1])
element6 = YachiElement(bp6,6,[1,1,1])
element7 = YachiElement(bp7,7,[1,1,1])
element8 = YachiElement(bp8,8,[1,1,1])

elements = [element1,element2,element3,element4,element5,element6,element7,element8]
def getOrientations():
    orientations = [list() for _ in range(8)]
    for m in range(0,8):
        ground_orientations = list()
        for i in range(1,5):
            for l in range(1,3):
                space = ThreeDimBlockSpace(4,4,4)
                space.setRoot([1,l,i])
                merged_space = space.merge(elements[m])
                ground_orientations.append(merged_space)
                orientations[m].append(merged_space)
        for ground_orientation in ground_orientations:
            new_space = ground_orientation
            for i in range(4):
                new_space = new_space.rotate('z')
                orientations[m].append(new_space)
            new_space = ground_orientation.rotate('x').rotate('x')
            for i in range(5):
                orientations[m].append(new_space)
                new_space = new_space.rotate('z')
            new_space = ground_orientation.rotate('x')
            for i in range(5):
                orientations[m].append(new_space)
                new_space = new_space.rotate('y')
            new_space = ground_orientation.rotate('x').rotate('x').rotate('x')
            for i in range(5):
                orientations[m].append(new_space)
                new_space = new_space.rotate('y')
            new_space = ground_orientation.rotate('y')
            for i in range(5):
                orientations[m].append(new_space)
                new_space = new_space.rotate('x')
            new_space = ground_orientation.rotate('y').rotate('y').rotate('y')
            for i in range(5):
                orientations[m].append(new_space)
                new_space = new_space.rotate('x')
    return orientations

        

