class SingleBlockElement:

    def __init__(self,*args):
        self.is_solid = bool()
        self.iD = int()
        
        if len(args)==1:
            self.iD = args[0]
            self.is_solid = True
        else:
            self.is_solid = False

    def setID(self,iD):
        self.iD = iD
        self.is_solid = True

    def unsolidify(self):
        self.iD = int()
        self.is_solid = False

    def __str__(self):
        if self.is_solid:
            return ("ID: " + str(self.iD)).ljust(8,' ')
        else:
            return "no Solid"

class ThreeDimBlockSpace:
    def __init__(self,x_dim,y_dim,z_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim
        self.x_coords = range(1,x_dim+1)
        self.y_coords = range(1,y_dim+1)
        self.z_coords = range(1,z_dim+1)
        self.block_space = [[[SingleBlockElement() for _ in range(x_dim)] for _ in range(y_dim)]for _ in range(z_dim)]
        self.root = [int()*3]

    def addBlock(self,x,y,z,iD):
        self.block_space[z-1][y-1][x-1].setID(iD)
    def delBlock(self,x,y,z):
        self.block_space[z-1][y-1][x-1].unsolidify()
    def getBlock(self,x,y,z):
        return self.block_space[z-1][y-1][x-1]

    def setRoot(self,root):
        self.root = root
    def __str__(self):
        stri = "\nsliced from top to bottom...\n" + "".ljust(11*self.x_dim, '-') + "\n"
        for z in range(self.z_dim):
            stri = stri + "\nLayer %d:" %(z+1) + "\n"
            for y in range(self.y_dim):
                for x in range(self.x_dim):
                    stri = stri + str(self.block_space[z][y][x]) + " | "
                stri = stri + "\n"
        return stri
    def __add__(self,other):

        new_block_space = ThreeDimBlockSpace(self.x_dim,self.y_dim,self.z_dim)

        if type(other) == ThreeDimBlockSpace:
            pass
        else:
            other = other.geometry
        
        if self.x_dim == other.x_dim and self.y_dim == other.y_dim and self.z_dim == other.z_dim:
            for z in self.z_coords:
                for y in self.y_coords:
                    for x in self.x_coords:
                        if self.getBlock(x,y,z).is_solid == False and other.getBlock(x,y,z).is_solid == True:
                            new_block_space.addBlock(x,y,z,other.getBlock(x,y,z).iD)
                        elif self.getBlock(x,y,z).is_solid == True and other.getBlock(x,y,z).is_solid == True:
                            return None
                        elif self.getBlock(x,y,z).is_solid == True and other.getBlock(x,y,z).is_solid == False:
                            new_block_space.addBlock(x,y,z,self.getBlock(x,y,z).iD)
        return new_block_space

    def merge(self,other):
        merged_block_space = ThreeDimBlockSpace(self.x_dim,self.y_dim,self.z_dim)
        if type(other) == ThreeDimBlockSpace:
            pass
        else:
            other = other.geometry
        
        if other.x_dim - other.root[0] <= self.x_dim - self.root[0] and other.root[0] <= self.root[0]:
            pass
        else:
            print("Block_Space_Error: ""out of bounds in x""")
            return
        if other.y_dim - other.root[1] <= self.y_dim - self.root[1] and other.root[1] <= self.root[1]:
            pass
        else:
            print("Block_Space_Error: ""out of bounds in y""")
            return
        if other.z_dim - other.root[2] <= self.z_dim - self.root[2] and other.root[2] <= self.root[2]:
            pass
        else:
            print("Block_Space_Error: ""out of bounds in z""")
            return
        
        x_offset = other.root[0] - self.root[0]
        y_offset = other.root[1] - self.root[1]
        z_offset = other.root[2] - self.root[2]

        for z in self.z_coords:
            for y in self.y_coords:
                for x in self.x_coords:
                    if (x + x_offset >=1 and x + x_offset <= other.x_dim and
                        y + y_offset >=1 and y + y_offset <= other.y_dim and
                        z + z_offset >=1 and z + z_offset <= other.z_dim):
                        if other.getBlock(x + x_offset,y + y_offset, z + z_offset).is_solid == True and self.getBlock(x,y,z).is_solid == False:
                            merged_block_space.addBlock(x,y,z,other.getBlock(x + x_offset,y + y_offset, z + z_offset).iD)
                        if other.getBlock(x + x_offset,y + y_offset, z + z_offset).is_solid == False and self.getBlock(x,y,z).is_solid == True:
                            merged_block_space.addBlock(x,y,z,self.getBlock(x,y,z).iD)
                        if other.getBlock(x + x_offset,y + y_offset, z + z_offset).is_solid == True and self.getBlock(x,y,z).is_solid == True:
                            print("Block_Space_Error: ""Overlapping""")
                    if self.getBlock(x,y,z).is_solid == True:
                        merged_block_space.addBlock(x,y,z,self.getBlock(x,y,z).iD)
        return merged_block_space

    def rotate(self,axe):
        rotated_block_space = ThreeDimBlockSpace(self.x_dim,self.y_dim,self.z_dim)
        if axe == 'z':
            if self.x_dim == self.y_dim:
                pass
            else:
                print("Block_Space_Error: ""No rotational symmetrie around z-axe""")
            edge = self.x_dim+1
            for z in self.z_coords:
                for y in self.y_coords:
                    for x in self.x_coords:
                        if self.getBlock(x,y,z).is_solid == True:
                            new_x = y
                            new_y = edge - x
                            rotated_block_space.addBlock(new_x,new_y,z,self.getBlock(x,y,z).iD)
        if axe == 'x':
            if self.y_dim == self.z_dim:
                pass
            else:
                print("Block_Space_Error: ""No rotational symmetrie around x-axe""")
            edge = self.y_dim+1
            for z in self.z_coords:
                for y in self.y_coords:
                    for x in self.x_coords:
                        if self.getBlock(x,y,z).is_solid == True:
                            new_y = z
                            new_z = edge - y
                            rotated_block_space.addBlock(x,new_y,new_z,self.getBlock(x,y,z).iD)
        if axe == 'y':
            if self.z_dim == self.x_dim:
                pass
            else:
                print("Block_Space_Error: ""No rotational symmetrie around y-axe""")
            edge = self.y_dim+1
            for z in self.z_coords:
                for y in self.y_coords:
                    for x in self.x_coords:
                        if self.getBlock(x,y,z).is_solid == True:
                            new_z = x
                            new_x = edge - z
                            rotated_block_space.addBlock(new_x,y,new_z,self.getBlock(x,y,z).iD)
                            
                            
        return rotated_block_space



class YachiElement:

    def __init__(self,blue_print,iD,root):
        self.iD = iD
        self.blue_print = blue_print
        self.geometry = ThreeDimBlockSpace(4,3,1)
        self.root = root
        self.build_geometry()

    def build_geometry(self):
        self.geometry.setRoot(self.root)
        for y in range(len(self.blue_print)):
            for x in range(len(self.blue_print[y])):
                if self.blue_print[y][x] == 1:
                    self.geometry.addBlock(x+1,y+1,1,self.iD)
    def __str__(self):
        return str(self.geometry) 
def test():
    bp1 = [[1,1,1,1],
        [0,1,1,0],
        [0,1,1,0]]
    element1 = YachiElement(bp1,1,[1,1,1])
    print(element1)
    build_space = ThreeDimBlockSpace(4,4,4)
    build_space.setRoot([1,1,4])
    build_space = build_space.merge(element1.geometry)
    new_space = build_space
    new_space = new_space.rotate('x')
    print(build_space)
    print(new_space)