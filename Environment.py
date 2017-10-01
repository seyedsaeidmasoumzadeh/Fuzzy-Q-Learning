import math


class Environment(object):
    action_set = []
    state = []

    def __init__(self):
        # cart position in the horizontal direction x = state[0], and cart velocity denoted by x_ = state[1]
        # vertical angle of the pole denoted by tetha = state[2], angular velocity of the pole tetha_ = state[3]
        self.state = [0,0,0,0]
        self.action_set = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0 ,1,2,3,4,5,6,7,8,9,10]

    def apply_action(self,action):
        u = self.action_set[action]
        self.get_current_state(u)
        reward = self.get_reward()
        return reward, self.state

    def get_state_variable(self,variable_name):

        if variable_name == 'x':
            return self.state[0]
        elif variable_name == "x_":
            return self.state[1]
        elif variable_name == "tetha":
            return self.state[2]
        else:
            return self.state[3]

    def set_state_variable(self,variable_name,value):

        if variable_name == 'x':
            self.state[0] = value
        elif variable_name == "x_":
            self.state[1] = value
        elif variable_name == "tetha":
            self.state[2] = value
        elif variable_name == "tetha_":
            self.state[3] = value

    def get_current_state(self,u):
        mio_c = 0.000002
        mio_p = 0.0005
        m_big = 1
        m = 0.1
        l = 0.5
        g = 9.8
        # The dynamics of the cart-pole system
        theta__ = ((g * math.sin(self.get_state_variable('tetha')) - math.cos(self.get_state_variable('tetha'))) * (u + (m * l * math.pow(self.get_state_variable('tetha_'),2) * math.sin(self.get_state_variable('tetha'))) - (mio_c * math.copysign(self.get_state_variable('x_'),1))) - mio_p * g * math.sin(self.get_state_variable('tetha')) - math.cos(self.get_state_variable('tetha')) * (u + (m * l * math.pow(self.get_state_variable('tetha_'),2) * math.sin(self.get_state_variable('tetha'))) - (mio_c * math.copysign(1,self.get_state_variable('x_')))) - ((mio_p * self.get_state_variable('tetha_'))/(m*l))) / (l * ((4/3) - ((m * math.pow(math.cos(self.get_state_variable('tetha')), 2))/ m_big + m)))
        x__= (u + ((m * l) * ((math.pow(self.get_state_variable('tetha_'),2)*math.sin(self.get_state_variable('tetha'))) - (theta__ * math.cos(self.get_state_variable('tetha'))))) - (mio_c * math.copysign(self.get_state_variable('x_'),1))) / (m_big + m)
        self.set_state_variable('x', self.get_state_variable('x') + (self.get_state_variable('x_') * 0.02))
        self.set_state_variable('x_', self.get_state_variable('x_') + (x__ * 0.02))
        self.set_state_variable('tetha', self.get_state_variable('tetha') + (self.get_state_variable('tetha_') * 0.02))
        self.set_state_variable('tetha_', self.get_state_variable('tetha_') + (theta__ * 0.02))

    def get_reward(self):
        if (math.copysign(self.get_state_variable('x'),1) > 2.4) or (math.copysign(self.get_state_variable('tetha'),1) > 0.2094):
            reward = -1
        else:
            reward = 0
        return reward

