from pyomo.environ import *

#MyModel1 = AbstractModel()

MyModel = ConcreteModel() 

#set
MyModel.IDX = RangeSet(3) # 1 , 2 , 3

#variable

MyModel.x = Var( MyModel.IDX , within = NonNegativeReals)   #Binary, NonNegativeInteger , ....

#Objective Function

MyModel.obj = Objective( expr= 2*MyModel.x[1] + 3*MyModel.x[2]+ MyModel.x[3], sense = minimize)

#Constraints

MyModel.ST = ConstraintList()

MyModel.ST.add(MyModel.x[1] + 2*MyModel.x[2] +2*MyModel.x[3] >= 3)
MyModel.ST.add(2* MyModel.x[1] + 3*MyModel.x[2] + 4*MyModel.x[3] <= 6)

solver = SolverFactory('ipopt') #solver name
solver.solve(MyModel)
display(MyModel)