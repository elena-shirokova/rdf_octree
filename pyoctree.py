
# -*- coding: utf-8 -*-
#python octree implementation
# Code © Spencer Krum June 2011
# Released underl GPLv3 See LICENSE file in this repository

class node():
    """
    Class to be a node in my octree
    """

    def __init__(self,parent, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit):
        self.parent = parent
        self.Xupperlimit = Xupperlimit
        self.Yupperlimit = Yupperlimit
        self.Zupperlimit = Zupperlimit
        self.Xlowerlimit = Xlowerlimit
        self.Ylowerlimit = Ylowerlimit
        self.Zlowerlimit = Zlowerlimit
        self.Xcenter = (self.Xupperlimit + self.Xlowerlimit)/2.
        self.Ycenter = (self.Yupperlimit + self.Ylowerlimit)/2.
        self.Zcenter = (self.Zupperlimit + self.Xlowerlimit)/2.

    parent = None
    value = None

    #children
    posXposYposZ = None
    posXposYnegZ = None
    posXnegYposZ = None
    posXnegYnegZ = None
    negXposYposZ = None
    negXposYnegZ = None
    negXnegYposZ = None
    negXnegYnegZ = None

    #array of children
    chidren = [posXposYposZ,posXposYnegZ,posXnegYposZ,posXnegYnegZ,negXposYposZ,negXposYnegZ,negXnegYposZ,negXnegYnegZ]

    #position in space
    Xupperlimit = None
    Yupperlimit = None
    Zupperlimit = None

    Xlowerlimit = None
    Ylowerlimit = None
    Zlowerlimit = None
    def get_array_of_children(self):
        """
        helper function to return array of children
        because there is some weird issue where just setting an
        array variable isn't cutting it
        """
        children = [self.posXposYposZ,self.posXposYnegZ,self.posXnegYposZ,self.posXposYnegZ,self.negXposYposZ,self.negXposYnegZ,self.negXnegYposZ,self.negXnegYnegZ ]
        return children

    def print_types(self):
       for child in chidren:
            print type(self.child)


    def print_info(self):
        """
        helper function to dump node paramaters
        """

        print "parent:\t {0}".format(self.parent)
        print "value:\t {0}".format(self.value)

        #children
        print "posXposYposZ: \t {0}".format(self.posXposYposZ)
        print "posXposYnegz: \t {0}".format(self.posXposYnegZ)
        print "posXnegYposZ: \t {0}".format(self.posXnegYposZ)
        print "posXnegYnegZ: \t {0}".format(self.posXnegYnegZ)
        print "negXposYposZ: \t {0}".format(self.negXposYposZ)
        print "negXposYnegZ: \t {0}".format(self.negXposYnegZ)
        print "negXnegYposZ: \t {0}".format(self.negXnegYposZ)
        print "negXnegYnegZ: \t {0}".format(self.negXnegYnegZ)

        #position in space
        print "Xupperlimit: \t {0}".format(self.Xupperlimit)
        print "Yupperlimit: \t {0}".format(self.Yupperlimit)
        print "Zupperlimit: \t {0}".format(self.Zupperlimit)

        print "Xlowerlimit: \t {0}".format(self.Xlowerlimit)
        print "Ylowerlimit: \t {0}".format(self.Ylowerlimit)
        print "Zlowerlimit: \t {0}".format(self.Zlowerlimit)

        print "Xcenter: \t {0}".format(self.Xcenter)
        print "Ycenter: \t {0}".format(self.Ycenter)
        print "Zcenter: \t {0}".format(self.Zcenter)


    def add(self, payload, coord, level):

        """
        Create a subnode
        """

        if level == 0:
            try:
                self.value.append((coord,payload))
            except AttributeError:
                self.value = []
                self.value.append((coord,payload))

        else:
            level -= 1
            #Determine quadrant
            if coord[0] <= self.Xcenter:
                #negX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.negXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYnegZ.add(payload, coord, level)
                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.negXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYposZ.add(payload, coord, level)
                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.negXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.negXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYposZ.add(payload, coord, level)


            else:
                #posX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.posXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.posXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYposZ.add(payload, coord, level)

                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Zcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.posXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.posXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYposZ.add(payload, coord, level)



class Octree():
    """
    class to hold the whole tree
    """

    def __init__(self, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin, root_coords=(0,0,0), maxiter=7):
        self.Xmax = Xmax
        self.Ymax = Ymax
        self.Zmax = Xmax
        self.Xmin = Xmin
        self.Ymin = Ymin
        self.Zmin = Zmin
        self.root_coords = root_coords
        self.maxiter = maxiter

        self.root = node('root', Xmax, Ymax, Zmax, Xmin, Ymin, Zmin)

    def add_item(self, payload, coord):
        """
        Create recursively create subnodes until maxiter is reached
        then deposit payload in that node
        """

        self.root.add(payload, coord, self.maxiter)

    def find_within_range(self, center, size, shape):
        """
        Return payloads and coordinates of every payload within
        a specified area
        """
        """
        When shape is cube:
        Search space is defined as the cubic region where each face is 'size'
        distance directly away from the center.
        """
        """
        Should support "cube", "sphere", "doughnut"
        """
        if shape == "cube":



            payloads = []
            templist = [self.root]
            list_list = []
            list_list.append([self.root])
            for level in range(self.maxiter):
                list_list.append([])

            print list_list
            for level in range(self.maxiter):
                for node in list_list[level]:
                    Xedge_max = center[0] + size
                    Xedge_min = center[0] - size
                    Yedge_max = center[1] + size
                    Yedge_min = center[1] - size
                    Zedge_max = center[2] + size
                    Zedge_min = center[2] - size

                    corner0 = (Xedge_max, Yedge_max, Zedge_max)
                    corner1 = (Xedge_max, Yedge_max, Zedge_min)
                    corner2 = (Xedge_max, Yedge_min, Zedge_max)
                    corner3 = (Xedge_max, Yedge_min, Zedge_min)
                    corner4 = (Xedge_min, Yedge_max, Zedge_max)
                    corner5 = (Xedge_min, Yedge_max, Zedge_min)
                    corner6 = (Xedge_min, Yedge_min, Zedge_max)
                    corner7 = (Xedge_min, Yedge_min, Zedge_min)
                    corners = [corner0, corner1, corner2, corner3, corner4, corner5, corner6, corner7]
                    table = ((corner0[0] > node.Xcenter),(corner0[1] > node.Ycenter) ,(corner0[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXposYposZ)
                    table = ((corner1[0] > node.Xcenter),(corner1[1] > node.Ycenter) ,(corner1[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXposYnegZ)
                    table = ((corner2[0] > node.Xcenter),(corner2[1] < node.Ycenter) ,(corner2[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXnegYposZ)
                    table = ((corner3[0] > node.Xcenter),(corner3[1] < node.Ycenter) ,(corner3[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.posXnegYnegZ)
                    table = ((corner4[0] < node.Xcenter),(corner4[1] > node.Ycenter) ,(corner4[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXposYposZ)
                    table = ((corner5[0] < node.Xcenter),(corner5[1] > node.Ycenter) ,(corner5[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXposYnegZ)
                    table = ((corner6[0] < node.Xcenter),(corner6[1] < node.Ycenter) ,(corner6[2] > node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXnegYposZ)
                    table = ((corner7[0] < node.Xcenter),(corner7[1] < node.Ycenter) ,(corner7[2] < node.Zcenter))
                    if not False in table:
                        list_list[level+1].append(node.negXnegYnegZ)


                    #must remove children that aren't real yet
                    temp_templist = []
                    for node in list_list[level+1]:
                        try:
                           node.Xcenter
                           temp_templist.append(node)
                        except AttributeError:
                            pass
                    list_list[level+1] = temp_templist


            payloads = [i.value for i in list_list[-1]]
            return payloads



def find_closest_three(x, y, z, tree):
    """
    function to find the closest three data points to
    a given data point
    """
    #brief sanity checking
    if (x >= tree.Xmax or x <= tree.Xmin):
        print "Fail, out of range"
    if (y >= tree.Ymax or y <= tree.Ymin):
        print "Fail, out of range"
    if (z >= tree.Zmax or z <= tree.Zmin):
        print "Fail, out of range"

    #find the node by coords
    for level in range(tree.maxiter):
        pass



if __name__ == "__main__":


    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    tree = Octree(100,100,100, -100, -100, -100)
    data = [(random.randrange(5,200),random.randrange(5,200),random.randrange(5,200)) for i in xrange(0,10000)]
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = np.linspace(0, 1, 100)
    y = 20 + 3 * x + np.random.normal(0, 60, 100)
    ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')

    colors = ('r', 'g', 'b', 'k')
    for c in colors:
        xmax = tree.Xmax
        xmin = tree.Ymax

        y = np.random.sample(20)
        z = np.random.sample(20)
        ax.scatter(xmax, xmin, 0, zdir='y', c=c)

    ax.legend()
    ax.set_xlim3d(0, 100)
    ax.set_ylim3d(0, 100)
    ax.set_zlim3d(0, 100)

    plt.show()


    print data


    for triple in data:
        tree.add_item('depr',triple)
        print "success"
        plt.plot(triple)

    #plt.plot()

    #def drawbox(x,y,z,x1,y1,z1,color):

    #def draw_oct(node):


    #get some data
    entries = tree.find_within_range((0,0,0), 40, "cube")
    for i in entries:
        print i




