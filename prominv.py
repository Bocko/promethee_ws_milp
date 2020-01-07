from pulp import *
from promethee import *

def prominv_w(criteria, init_weights, funcPrefCrit, names, alternatives, FIRST, MODIF):
    uninetflows = uninetflows_eval(alternatives,criteria,init_weights,funcPrefCrit)

    uniposflows, uninegflows = uniflows_eval(alternatives, criteria, funcPrefCrit)

    walking_weights = walking_weights_eval(uninetflows,init_weights)

    # si_weights, si_rankings, si_firsts, si_diffs = si_weights_update(walking_weights,init_weights,alternatives,criteria,funcPrefCrit)

    def netflow_eval(a,w):
        return lpSum([uninetflows[a][i]*w[i] for i in range(len(w))])

    def posflow_eval(a,w):
        return lpSum([uniposflows[a][i]*w[i] for i in range(len(w))])

    def negflow_eval(a,w):
        return lpSum([uninegflows[a][i]*w[i] for i in range(len(w))])

    # Problem definition
    prob = LpProblem("IPO",LpMinimize)

    # Constants
    EPS = 1e-6  # To avoid ties
    M = 1e6
    criteria = range(len(init_weights))
    alts = range(len(uninetflows))

    # Variables
    new_weights = LpVariable.dicts("Weight",criteria,lowBound=0,upBound=1,cat="Continuous")
    d1 = LpVariable.dicts("d1",criteria,lowBound=0,upBound=1,cat="Continuous")
    d2 = LpVariable.dicts("d2",criteria,lowBound=0,upBound=1,cat="Continuous")
    delta = LpVariable.dicts("delta",criteria,cat="Binary")
    alpha = LpVariable.dicts("alpha",criteria,cat="Binary")

    # Objective function
    prob += lpSum([d1[i]+d2[i] for i in criteria])

    # Constraints
    prob += lpSum(new_weights) == 1, "Weigths constraint"

    for i in criteria:
        # Absolute value lin
        prob += delta[i] >= 0.5*(init_weights[i] - new_weights[i]) + EPS
        prob += delta[i] <= 0.5*(init_weights[i] - new_weights[i]) + 1
        prob += init_weights[i] - new_weights[i] == d1[i] - d2[i]
        prob += 0 <= d1[i]
        prob += d1[i] - delta[i] <= 0
        prob += 0 <= d2[i]
        prob += d2[i] <= 1-delta[i]

        prob += alpha[i] >= d1[i] + d2[i]
        prob += alpha[i] <= M*(d1[i] + d2[i])

    prob += lpSum([alpha[i] for i in criteria]) <= MODIF

    # Rank change PII
    for j in alts:
        if j != FIRST:
            prob += netflow_eval(FIRST,new_weights) >= netflow_eval(j,new_weights) + EPS

    # Rank change PI
    # for j in alts:
    #     if j != FIRST:
    #         prob += posflow_eval(FIRST,new_weights) >= posflow_eval(j,new_weights) + EPS
    #         prob += negflow_eval(FIRST,new_weights) <= negflow_eval(j,new_weights) - EPS

    prob.solve()

    return prob

