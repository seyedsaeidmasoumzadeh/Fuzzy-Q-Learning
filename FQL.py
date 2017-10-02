import numpy as np
import FIS
import operator
import itertools
import functools
import random
import sys
import copy


class Model(object):
    L = []
    R = []
    R_= []
    M = []
    Q = 0
    V = 0
    Error = 0
    q_table = np.matrix([])

    def __init__(self, gamma, alpha, ee_rate, q_initial_value, action_set_length,
                 fis = FIS.Build()):
        self.gamma = gamma
        self.alpha = alpha
        self.ee_rate = ee_rate
        self.q_initial_value = q_initial_value
        self.action_set_length = action_set_length
        self.fis = fis
        if self.q_initial_value =='random':
            self.q_table = np.random.random((self.fis.get_number_of_rules(), self.action_set_length))
        if self.q_initial_value == 'zero':
            self.q_table = np.zeros((self.fis.get_number_of_rules(), self.action_set_length))

    def CalculateTruthValue(self,state_value):
        self.R = []
        self.L = []
        input_variables = self.fis.list_of_input_variable
        for index, variable in enumerate(input_variables):
            X =[]
            fuzzy_sets = variable.get_fuzzy_sets()
            for set in fuzzy_sets:
                membership_value = set.membership_value(state_value[index])
                X.append(membership_value)
            self.L.append(X)
        for element in itertools.product(*self.L):
            self.R.append(functools.reduce(operator.mul, element, 1))

    def ActionSelection(self):
        self.M = []
        r = random.uniform(0, 1)
        max = -sys.maxsize
        for rull in self.q_table:
            if r < self.ee_rate:
                for index , action in enumerate(rull):
                    if action > max:
                        action_index = index
            else:
                action_index = random.randint(0, self.action_set_length -1)
            self.M.append(action_index)

    def InferredAction(self):
        max = -sys.maxsize
        for index , truth_value in enumerate(self.R):
            if truth_value > max:
                max = truth_value
                action = self.M[index]
        return action

    def CalculateQValue(self):
        self.Q = 0
        for index, truth_value in enumerate(self.R):
            self.Q = self.Q + truth_value * self.q_table[index,self.M[index]]
        self.Q = self.Q / sum(self.R)

    def CalculateStateValue(self):
        self.V = 0
        max = -sys.maxsize
        for index, rull in enumerate(self.q_table):
            for action in rull:
                if action < max:
                    max = action
            self.V = (self.R[index] * max) + self.V
        if sum(self.R) == 0:
            self.R[0] = 0.00001
        self.V = self.V / sum(self.R)

    def CalculateQualityVariation(self, reward):
        self.Error = reward + ((self.gamma * self.V) - self.Q)

    def UpdateqValue(self):
        for index, truth_value in enumerate(self.R_):
            delta_Q = self.alpha * (self.Error * truth_value)
            self.q_table[index][self.M[index]] = self.q_table[index][self.M[index]] + delta_Q

    def KeepStateHistory(self):
        self.R_ = copy.copy(self.R)


    def get_initial_action(self,state):
        self.CalculateTruthValue(state)
        self.ActionSelection()
        action = self.InferredAction()
        self.CalculateQValue()
        self.KeepStateHistory()
        return action

    def run(self,state, reward):
        self.CalculateTruthValue(state)
        self.CalculateStateValue()
        self.CalculateQualityVariation(reward)
        self.UpdateqValue()
        self.ActionSelection()
        action = self.InferredAction()
        self.CalculateQValue()
        self.KeepStateHistory()
        return action



