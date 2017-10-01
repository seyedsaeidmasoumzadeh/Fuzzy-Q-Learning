import FuzzySet
import StateVariable
import FQL
import FIS
from Environment import Environment
import matplotlib.pyplot as plt


# Create FIS
x1 = StateVariable.InputStateVariable(FuzzySet.Trapeziums(-2.4, -2, -1, -0.5), FuzzySet.Trapeziums(-1, -0.5, 0.5 , 1), FuzzySet.Trapeziums(0.5, 1, 2, 2.4) )
x2 = StateVariable.InputStateVariable(FuzzySet.Triangles(-2.4,-0.5,1), FuzzySet.Triangles(-0.5,1,2.4))
x3 = StateVariable.InputStateVariable(FuzzySet.Triangles(-3.14159, -1.5, 0), FuzzySet.Triangles(-1.5, 0, 1.5), FuzzySet.Triangles(0, 1.5, 3.1459))
x4 = StateVariable.InputStateVariable(FuzzySet.Triangles(-3.14159, -1.5, 0), FuzzySet.Triangles(-1.5, 0, 1.5), FuzzySet.Triangles(0, 1.5, 3.1459))
fis = FIS.Build(x1,x2,x3,x4)


# Create Model
angel_list = []
model = FQL.Model(gamma = 0.9, alpha = 0.1 , ee_rate = 0.999, q_initial_value = 'random',
                  action_set_length = 21, fis = fis)
env = Environment()
for iteration in range (0,5000):
    if iteration % 100 == 0 or reward == -1:
        env.__init__()
        action = model.get_initial_action(env.state)
        reward, state_value = env.apply_action(action)
    action = model.run(state_value, reward)
    reward, state_value = env.apply_action(action)
    if reward != -1:
        angel_list.append(state_value[2])

plt.figure(figsize=(14,3))
plt.plot(angel_list)
plt.ylabel('Pole Angel')
plt.show()









