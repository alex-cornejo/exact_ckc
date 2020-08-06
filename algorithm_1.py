from gurobipy import *
import math
import numpy as np
import heapq

def heap_sort(items):
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]
    return items

def createGraph(input_file):
    global n, m , k, matrix, ordered_sizes, L, capacity
    f = open(input_file, "r")
    m = n
    matrix = []
    capacity = []
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

    ordered_sizes = []
    for i in range(0, n):
        for j in range(i, n):
            ordered_sizes.append(matrix[i][j])
    ordered_sizes = heap_sort(ordered_sizes)
    
        
    
def run(r):
    global total_runtime, k, runtime, num_centers, m, capacity, input_file, L
    prunedMatrix = []
    for i in range(0,n):
        list = []
        for j in range(0,n):
            list.append(float(0))
        prunedMatrix.append(list)
    for i in range(0,n):
        for j in range(0,n):
            if matrix[i][j] <= r:
                prunedMatrix[i][j] = 1
            if i == j:
                prunedMatrix[i][j] = 0
    
    try:
        global m, num_centers, runtime, capacity
        m = Model("mip1")
        
        #m.Params.outputFlag = 0
        
        m.setParam("MIPGap", 0.0);
        
        m.params.BestObjStop = k
        
        y = []
        for i in range(n):
            y.append(0)
        
        for i in range(n):
            y[i] = m.addVar(vtype=GRB.BINARY, name="y%s" % str(i+1))
        
        m.setObjective(quicksum(y), GRB.MINIMIZE)
        
        temp_list = np.array(prunedMatrix).T.tolist()
    
        
        x = []
        
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            x.append(temp)
        
        for i in range(n):
            for j in range(n):
                x[i][j] = m.addVar(vtype=GRB.BINARY, name="x%s%s" % (str(i+1), str(j+1)))
        
        temp_list_2 = np.array(x).T.tolist()
        
        if L == 'NA':
            for i in range(n):
                m.addConstr(quicksum(temp_list_2[i]) <= capacity[i])
        else:
            L = int(L)
            for i in range(n):
                m.addConstr(quicksum(temp_list_2[i]) <= L)
    
        for i in range(n):
            for j in range(n):    
                m.addConstr(x[i][j] <= y[j])
                
        for i in range(n):
            for j in range(n):    
                m.addConstr(x[i][j] <= prunedMatrix[i][j])
        
        for i in range(n):
            m.addConstr(quicksum(x[i]) == 1-y[i])
        
        m.optimize()
        runtime = m.Runtime
        print("The run time is %f" % runtime)
        print("Obj:", m.objVal)
        
        dom_set_size = 0
        solution = []
        assignment = []
        center = 0
        vertex_j = 1
        vertex_i = 1
        for v in m.getVars():
            varName = v.varName
            if varName[0] == 'y':
                if v.x >= 0.9:
                    dom_set_size = dom_set_size + 1
                    solution.append(varName[1:])
            else:
                if vertex_j <= n:
                    #if v.x == 1.0:
                    if v.x >= 0.9:
                        assignment.append([vertex_i, vertex_j])
                else:
                    vertex_i = vertex_i + 1
                    vertex_j = 1
                vertex_j = vertex_j + 1
        print("Cap. dom. set cardinality: " + str(dom_set_size))
        solution = [int(i) for i in solution] 
        #print("solution: " + str(solution))
        #print("assignment: " + str(assignment))
        
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
        
        num_centers = dom_set_size
#        num_centers = m.objVal
        
    except GurobiError:
        print("Error reported")
        
        
def binarySearch():
    global total_runtime, k, runtime, num_centers, input_file
    total_runtime = 0
    not_done = True
    upper = len(ordered_sizes) - 1
    lower = 0
    best_solution_size = float("inf")
    #while not_done:
    while upper - lower >= 1:
        mid = math.ceil((upper + lower) /2)
        mid_value = ordered_sizes[int(mid)]
        run(mid_value)
        total_runtime = total_runtime + runtime
        if mid == upper:
            lower = upper
        if num_centers <= k:
            upper = mid
            print("UPPER = MID")
            if mid_value <= best_solution_size:
                best_solution_size = mid_value
        else:
            lower = mid
            print("LOWER = MID")
        print("solution size: " + str(mid_value))
    print("best solution size: " + str(best_solution_size))    
    print("total runtime: " + str(total_runtime))
    
if __name__ == "__main__":
    global total_runtime, k, runtime, num_centers, L, n
    if len(sys.argv) != 5:
        print ("Wrong number of arguments")
        print ("exact input_file_path n k Q")
        sys.exit()
    input_file  = sys.argv[1]
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    L = sys.argv[4]
    createGraph(input_file)
    binarySearch()
