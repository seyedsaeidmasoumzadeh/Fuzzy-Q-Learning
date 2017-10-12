## Fuzzy-Q-Learning
A Python implementation of Fuzzy Q-Learning (FQL) for any controllers with continues states. As an example, the Pole Balancing problem (cartpole.py) has been implemented and it is inside this package.

## Implementation:
Fuzzy Q-Learning is a fuzzy extension of Q-learning algorithm. For creating an FQL model you first need to specify the input states and their corresponding fuzzy sets and then build your Fuzzy Inference System (FIS) to integrate with the Q-Learning algorithm. In this code, two type of fuzzy membership functions have been implemented : 1) Triangular and 2) Trapezoidal. For more information please read the following publications:
```
Masoumzadeh, S. S., Hlavacs, H., & Tomás, L. (2016, September). A Self-Adaptive Performance-Aware Capacity Controller in Overbooked Datacenters. In Cloud and Autonomic Computing (ICCAC), 2016 International Conference on (pp. 12-23). IEEE.

Jouffe, L. (1998). Fuzzy inference system learning by reinforcement methods. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 28(3), 338-355.
```


You can create as many as needed fuzzy sets, initialise them, and assign them to an input state variable to build your FIS as follows:
```
x1 = StateVariable.InputStateVariable(FuzzySet.Trapeziums(-2.4, -2, -1, -0.5), FuzzySet.Trapeziums(-1, -0.5, 0.5 , 1), FuzzySet.Trapeziums(0.5, 1, 2, 2.4) )
x2 = StateVariable.InputStateVariable(FuzzySet.Triangles(-2.4,-0.5,1), FuzzySet.Triangles(-0.5,1,2.4))
fis = FIS.Build(x1,x2)
```
Then you can buid your FQL model as follow:
```
model = FQL.Model(gamma = 0.9, alpha = 0.1 , ee_rate = 0.999, q_initial_value = 'zero', action_set_length = 21, fis = fis)
```

For creating your reward function, applying the action to the environment and getting new states. You just need to change Environment class inside the code.


## Licence

The code is published under the [MIT License]
