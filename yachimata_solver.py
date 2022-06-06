import threading
from yachimata_cube import *
from yachimata_orientations import *
import time
import os



def solve(l):
    clear = lambda: os.system('cls')
    clear()

    orientations = getOrientations()
    solution = ThreeDimBlockSpace(4,4,4)
    p = 0
    def statusLogger():
        while True:
            f = open("status_logger_%d.txt"%l,"w+")
            print ("%d__%d/240" %(l,p),end = '\r')
            f.write("%d/240" %(p))
            f.write(str(solution))
            time.sleep(10)


    x = threading.Thread(target=statusLogger, daemon=True)
    x.start()
    a = orientations[0][l-1]
    solutioni = solution + a
    if solutioni:
        solution = solutioni
        for b in orientations[1]:
            solutioni = solution + b
            p = p + 1
            if solutioni:
                solution = solutioni
                for c in orientations[2]:
                    solutioni = solution + c
                    if solutioni:
                        solution = solutioni
                        for d in orientations[3]:
                            solutioni = solution + d
                            if solutioni:
                                solution = solutioni
                                for e in orientations[4]:
                                    solutioni = solution + e
                                    if solutioni:
                                        solution = solutioni
                                        for f in orientations[5]:
                                            solutioni = solution + f
                                            if solutioni:
                                                solution = solutioni
                                                for g in orientations[6]:
                                                    solutioni = solution + g
                                                    if solutioni:
                                                        solution = solutioni
                                                        for h in orientations[7]:
                                                            solutioni = solution + h
                                                            if solutioni:
                                                                solution = solutioni
                                                                f = open("solution%d.txt"%l,"w+")
                                                                f.write(str(solution))
                                                                f.close()
                                                                f = open("status_logger_%d.txt"%l,"w+")
                                                                f.write("Done: \n ")
                                                                f.write(str(solution))
                                                                f.close()
                                                                print(solution)
                                                                quit()
                                                            
                                                        solution = ThreeDimBlockSpace(4,4,4) +a +b +c +d +e +f
                                                solution = ThreeDimBlockSpace(4,4,4) +a +b +c +d +e
                                        solution = ThreeDimBlockSpace(4,4,4) +a +b +c +d
                                solution = ThreeDimBlockSpace(4,4,4) +a +b +c
                        solution = ThreeDimBlockSpace(4,4,4) +a +b
                solution = ThreeDimBlockSpace(4,4,4) + a
                
        solution = ThreeDimBlockSpace(4,4,4)