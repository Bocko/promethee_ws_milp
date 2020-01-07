#!/usr/bin/env python3

from testproblem import *
from prominv import *

criteria_names, original_weights, func_pref_crit, alt_names, alt_eval = subset_bestcities()

ALT_FIRST = 6   # Index of alternative to rank first
ALLOWED_MODIF = len(original_weights)   # Number of allowed modification
prob = prominv_w(criteria_names, original_weights, func_pref_crit, alt_names, alt_eval, ALT_FIRST, ALLOWED_MODIF)

if prob.status:
    for v in prob.variables():
        if "Weight" in v.name:
            print(v.name, v.varValue)