import sys

sys.path.append("..")

from fuzzy_inference import fis, fuzzyset, state_variable
from environment import Environment
import fql

import matplotlib.pyplot as plt


# Create FIS
def main():
    x1 = state_variable.InputStateVariable(
        fuzzyset.Trapeziums(-2.4, -2, -1, -0.5),
        fuzzyset.Trapeziums(-1, -0.5, 0.5, 1),
        fuzzyset.Trapeziums(0.5, 1, 2, 2.4),
    )
    x2 = state_variable.InputStateVariable(
        fuzzyset.Triangles(-2.4, -0.5, 1), fuzzyset.Triangles(-0.5, 1, 2.4)
    )
    x3 = state_variable.InputStateVariable(
        fuzzyset.Triangles(-3.14159, -1.5, 0),
        fuzzyset.Triangles(-1.5, 0, 1.5),
        fuzzyset.Triangles(0, 1.5, 3.1459),
    )
    x4 = state_variable.InputStateVariable(
        fuzzyset.Triangles(-3.14159, -1.5, 0),
        fuzzyset.Triangles(-1.5, 0, 1.5),
        fuzzyset.Triangles(0, 1.5, 3.1459),
    )

    my_fis = fis.Build(x1, x2, x3, x4)
    # Create Model
    angel_list = []
    model = fql.Model(
        gamma=0.9,
        alpha=0.1,
        ee_rate=0.999,
        q_initial_value="random",
        action_set_length=21,
        fis=my_fis,
    )
    # Create Environment
    env = Environment()
    for iteration in range(0, 5000):
        if iteration % 100 == 0 or reward == -1:
            env.__init__()
            action = model.get_initial_action(env.state)
            reward, state_value = env.apply_action(action)
        action = model.run(state_value, reward)
        reward, state_value = env.apply_action(action)
        print(action, reward, state_value)
        if reward != -1:
            angel_list.append(state_value[2])

    plt.figure(figsize=(14, 3))
    plt.plot(angel_list)
    plt.ylabel("Pole Angel")
    plt.show()

if __name__ == "__main__":
    main()