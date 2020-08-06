from gurobipy import *
import math
import numpy as np

def createGraph(input_file):
    global n, m, L , k, matrix, capacity
    capacity = []
    f = open(input_file, "r")
    m = n
    matrix = []
    for i in range(0,n):
        list = []
        for j in range(0,n):
            list.append(float("inf"))
        matrix.append(list)
    positions = []
    for i in range(0, m):
        string = f.readline()
        string = string.split()
        temp_position = []
        temp_position.append(int(string[0])-1)
        temp_position.append(float(string[1]))
        temp_position.append(float(string[2]))
        positions.append(temp_position)
        if L == 'NA':
            capacity.append(float(string[3]))
        
    for i in range(0, n):
        for j in range(0, n):
            dist_temp = math.sqrt(((positions[i][1] - positions[j][1]) * (positions[i][1] - positions[j][1])) + ((positions[i][2] - positions[j][2]) * (positions[i][2] - positions[j][2])))
            matrix[i][j] = dist_temp
            matrix[j][i] = dist_temp
    f.close()
    for i in range(0, n):
        matrix[i][i] = 0
    
def run():
    global m, capacity, L
    try:
        global m, capacity, L
        m = Model("mip1")
        
        m.setParam("MIPGap", 0.0);
        
        y = []
        for i in range(n):
            y.append(0)
        
        for i in range(n):
            y[i] = m.addVar(vtype=GRB.BINARY, name="y%s" % str(i+1))
        
        x = []
        
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            x.append(temp)
        
        for i in range(n):
            for j in range(n):
                x[i][j] = m.addVar(vtype=GRB.BINARY, name="x%s%s" % (str(i+1), str(j+1)))

        z = m.addVar(vtype=GRB.CONTINUOUS, name="z")
        
        m.setObjective(z, GRB.MINIMIZE)
        
        for i in range(n):
            m.addConstr(quicksum(x[i]) == 1 - y[i])
            
        for i in range(n):
            for j in range(n):
                m.addConstr(x[i][j] <= y[j])
        
        m.addConstr(quicksum(y) <= k, "ck")
        
        for i in range(n):
            m.addConstr(quicksum(np.multiply(matrix[i], x[i]).tolist()) <= z)
            
            temp_list = np.array(x).T.tolist()
                
            if L == 'NA':
                m.addConstr(quicksum(temp_list[i]) <= capacity[i])
            else:
                L = int(L)
                m.addConstr(quicksum(temp_list[i]) <= L)
        
        #for i in range(n):
        #    m.addConstr(quicksum(temp_list[i]) <= L)
    
        m.optimize()
        runtime = m.Runtime
        
        solution = []
        assignment = []
        center = 0
        vertex_j = 1
        vertex_i = 1
        for v in m.getVars():
            varName = v.varName
            if varName[0] == 'y':
                if v.x >= 0.9:
                    solution.append(varName[1:])
            else:
                if vertex_j <= n:
                    if v.x >= 0.9:
                        assignment.append([vertex_i, vertex_j])
                else:
                    vertex_i = vertex_i + 1
                    vertex_j = 1
                vertex_j = vertex_j + 1
        solution = [int(i) for i in solution] 
        
        print('{"instance": "%s",' % input_file)
        print('"centers": [')
        counter = 0
        for center in solution:
            counter = counter + 1
            nodes = []
            for node in assignment:
                if node[1] == center:
                    nodes.append(node[0])
            if counter == len(solution):
                print('{ "center": ' + str(center) + ', "nodes": ' + str(nodes) + '}')
            else:
                print('{ "center": ' + str(center) + ', "nodes": ' + str(nodes) + '},')
        print(']}')
            
        print("Total runtime: %f" % runtime)
        print("Solution size:", m.objVal)
        
    except GurobiError:
        print("Error reported")
        
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print ("Wrong number of arguments")
        print ("tsp2lp input_file_path n k L")
        sys.exit()
    input_file  = sys.argv[1]
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    L = sys.argv[4]
    createGraph(input_file)
    run()
