from pyomo.environ import *

I = 3
J = 2
K = 3

M = ConcreteModel()


#Set

M.i = RangeSet(I)
M.j = RangeSet(J)
M.k = RangeSet(K)

#varabile

M.x = Var( M.i, M.j , M.k , within = NonNegativeReals)

#Objective

M.z = Objective( expr = (sum(M.x[i,j,k] for i in M.i for j in M.j for k in M.k) ), sense = maximize )

#Cosntraint

M.ST = Constraint( expr = M.x[1,1,1] <= 5)
M.cl = ConstraintList()

M.cl.add( (sum(M.x[3,j,k] for j in M.j for k in M.k ) <= 130 ) )
M.cl.add( (sum(M.x[i,1,3] for i in M.i) <= 60 ) )
M.cl.add( sum(M.x[i,j,k] for i in M.i for j in M.j for k in M.k) <= 200)

#Print

#M.pprint()

opt = SolverFactory('cplex_direct')
#opt = SolverFactory('glpk')
#opt = SolverFactory('ipopt')
results = opt.solve(M)
#display(M)

print("Optimal Value is shown below:")

print( value(M.z) )

print(" Variables are shown below:")
for i in M.i:
    for j in M.j:
        for k in M.k:
            print( "X[" , i , "," , j , "," , k ,"]:" , M.x[i,j,k].value)
            
