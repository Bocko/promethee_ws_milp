def netflows_eval(alternatives, weights, func_pref_crit):
    netflows = []
    if (len(alternatives) == 1):
            return alternatives[0]

    for alt1 in alternatives:
        outRankingPlus = 0
        outRankingMoins = 0
        for alt2 in alternatives:
            if alt1 == alt2:
                continue
            PiXA = 0
            PiAX = 0
            for k in range(len(func_pref_crit)):
                weight = weights[k]
                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                PiXA = PiXA + weight * funcPref.value(val1)
                PiAX = PiAX + weight * funcPref.value(val2)
            outRankingPlus = outRankingPlus + PiXA
            outRankingMoins = outRankingMoins + PiAX
        outRankingPlus = outRankingPlus / (len(alternatives) - 1)
        outRankingMoins = outRankingMoins / (len(alternatives) - 1)
        outRanking = outRankingPlus - outRankingMoins
        netflows.append(outRanking)

    return netflows

def nonorm_netflows_eval(alternatives, weights, func_pref_crit):
    netflows = []
    if (len(alternatives) == 1):
            return alternatives[0]

    for alt1 in alternatives:
        outRankingPlus = 0
        outRankingMoins = 0
        for alt2 in alternatives:
            if alt1 == alt2:
                continue
            PiXA = 0
            PiAX = 0
            for k in range(len(func_pref_crit)):
                weight = weights[k]
                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                PiXA = PiXA + weight * funcPref.value(val1)
                PiAX = PiAX + weight * funcPref.value(val2)
            outRankingPlus = outRankingPlus + PiXA
            outRankingMoins = outRankingMoins + PiAX
        # outRankingPlus = outRankingPlus / (len(alternatives) - 1)
        # outRankingMoins = outRankingMoins / (len(alternatives) - 1)
        outRanking = outRankingPlus - outRankingMoins
        netflows.append(outRanking)

    return netflows

def par_ranking_eval2(args):
    alternatives, weights, func_pref_crit, names = args

    netflows = []
    if (len(alternatives) == 1):
            return alternatives[0]

    for alt1 in alternatives:
        outRankingPlus = 0
        outRankingMoins = 0
        for alt2 in alternatives:
            if alt1 == alt2:
                continue
            PiXA = 0
            PiAX = 0
            for k in range(len(func_pref_crit)):
                weight = weights[k]
                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                PiXA = PiXA + weight * funcPref.value(val1)
                PiAX = PiAX + weight * funcPref.value(val2)
            outRankingPlus = outRankingPlus + PiXA
            outRankingMoins = outRankingMoins + PiAX
        outRankingPlus = outRankingPlus / (len(alternatives) - 1)
        outRankingMoins = outRankingMoins / (len(alternatives) - 1)
        outRanking = outRankingPlus - outRankingMoins
        netflows.append(outRanking)

    ranking = []
    sorted_netflows = []
    for i in sorted(enumerate(netflows), key=lambda x: x[1], reverse=True):
        ranking.append(names[i[0]])
        sorted_netflows.append(i[1])

    return ranking, sorted_netflows

def par_ranking_eval(weights):
    # alternatives, weights, func_pref_crit, names = args

    netflows = []
    if (len(alternatives) == 1):
            return alternatives[0]

    for alt1 in alternatives:
        outRankingPlus = 0
        outRankingMoins = 0
        for alt2 in alternatives:
            if alt1 == alt2:
                continue
            PiXA = 0
            PiAX = 0
            for k in range(len(func_pref_crit)):
                weight = weights[k]
                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                PiXA = PiXA + weight * funcPref.value(val1)
                PiAX = PiAX + weight * funcPref.value(val2)
            outRankingPlus = outRankingPlus + PiXA
            outRankingMoins = outRankingMoins + PiAX
        outRankingPlus = outRankingPlus / (len(alternatives) - 1)
        outRankingMoins = outRankingMoins / (len(alternatives) - 1)
        outRanking = outRankingPlus - outRankingMoins
        netflows.append(outRanking)

    ranking = []
    sorted_netflows = []
    for i in sorted(enumerate(netflows), key=lambda x: x[1], reverse=True):
        ranking.append(names[i[0]])
        sorted_netflows.append(i[1])

    return ranking, sorted_netflows

def netflows_to_ranking(names,netflows):
    ranking = []
    sorted_netflows = []
    for i in sorted(enumerate(netflows), key=lambda x: x[1], reverse=True):
        ranking.append(names[i[0]])
        sorted_netflows.append(i[1])

    return ranking, sorted_netflows

def uniflows_eval(alternatives, criteria, func_pref_crit):
    uniposflows = []
    uninegflows = []
    for alt1 in alternatives:
        uniposflows.append([])
        uninegflows.append([])
        for k in range(len(criteria)):
            uniposval = 0
            uninegval = 0
            for alt2 in alternatives:
                if alt1 == alt2:
                    continue

                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                uniposval += funcPref.value(val1)
                uninegval += funcPref.value(val2)

            uniposflows[-1].append(uniposval/(len(alternatives)-1))
            uninegflows[-1].append(uninegval/(len(alternatives)-1))

    return uniposflows, uninegflows

def nonorm_uniflows_eval(alternatives, criteria, func_pref_crit):
    uniposflows = []
    uninegflows = []
    for alt1 in alternatives:
        uniposflows.append([])
        uninegflows.append([])
        for k in range(len(criteria)):
            uniposval = 0
            uninegval = 0
            for alt2 in alternatives:
                if alt1 == alt2:
                    continue

                funcPref = func_pref_crit[k]
                valAlt1 = alt1[k]
                valAlt2 = alt2[k]
                val1 = valAlt1 - valAlt2
                val2 = valAlt2 - valAlt1
                uniposval += funcPref.value(val1)
                uninegval += funcPref.value(val2)

            uniposflows[-1].append(uniposval)
            uninegflows[-1].append(uninegval)

    return uniposflows, uninegflows

def uninetflows_eval(alternatives, criteria, weights, func_pref_crit):
    uniposflows, uninegflows = uniflows_eval(alternatives, criteria, func_pref_crit)
    uninetflows = [[0 for col in range(len(uniposflows[0]))] for row in range(len(uniposflows))]
    for i in range(len(uninetflows)):
        for j in range(len(uninetflows[0])):
            uninetflows[i][j] += uniposflows[i][j] - uninegflows[i][j]
    return uninetflows

def nonorm_uninetflows_eval(alternatives, criteria, weights, func_pref_crit):
    uniposflows, uninegflows = nonorm_uniflows_eval(alternatives, criteria, func_pref_crit)
    uninetflows = [[0 for col in range(len(uniposflows[0]))] for row in range(len(uniposflows))]
    for i in range(len(uninetflows)):
        for j in range(len(uninetflows[0])):
            uninetflows[i][j] += uniposflows[i][j] - uninegflows[i][j]
    return uninetflows

def walking_weights_eval(uninetflows, weights):
    crits = len(weights)
    alts = len(uninetflows)
    netflows = [sum([uninetflows[i][k]*weights[k] for k in range(crits)]) for i in range(alts)]
    ranking = sorted(range(alts), key=lambda k: netflows[k], reverse=True)
    # delta = netflows[a] - netflows[b]
    # delta_i = uninetflows[a][4] - uninetflows[b][4]
    # print("Test")
    # print(delta,delta_i)
    # print("calc",delta*delta_i < 0)
    # print("calc",delta*delta_i > delta**2)
    # print(delta*delta_i/(delta*delta_i-delta**2))
    omega_zero = [[] for i in range(crits)]
    omega_minus = [[] for i in range(crits)]
    omega_plus = [[] for i in range(crits)]
    alphas_minus = [[] for i in range(crits)]
    alphas_plus = [[] for i in range(crits)]
    walking_weights = []
    for k in range(crits):
        for i in ranking[:1]:
            for j in ranking:
                if i != j:
                    delta = netflows[i] - netflows[j]
                    delta_i = uninetflows[i][k] - uninetflows[j][k]
                    if delta*delta_i < 0 and (i,j) not in omega_minus[k]:
                        omega_minus[k].append((i,j))
                        alphas_minus[k].append(delta*delta_i/(delta*delta_i-delta**2))
                    elif delta*delta_i > delta**2 and (i,j) not in omega_plus[k]:
                        omega_plus[k].append((i,j))
                        alphas_plus[k].append(delta*delta_i/(delta*delta_i-delta**2))
                    elif delta == 0 and delta_i != 0 and (i,j) not in omega_zero[k]:
                        # TODO: non-empty case to develop
                        omega_zero[k].append((i,j))

        if omega_zero[k] != []:
            print("warning")

        if alphas_plus[k] == []:
            w_minus = 0
        else:
            alpha_plus = min(alphas_plus[k])
            beta_minus = (1-weights[k])/weights[k]*(1-alpha_plus)
            w_minus = (1+beta_minus)*weights[k]
            if w_minus < 0:
                w_minus = 0

        if alphas_minus[k] == []:
            w_plus = 1
        else:
            alpha_minus = max(alphas_minus[k])
            beta_plus = (1-weights[k])/weights[k]*(1-alpha_minus)
            w_plus = (1+beta_plus)*weights[k]
            if w_plus > 1:
                w_plus = 1

        walking_weights.append((w_minus,w_plus))

    return walking_weights

def weights_update(init_weights, new_weight, crit):
    crits = len(init_weights)
    beta = (new_weight-init_weights[crit])/init_weights[crit]
    alpha = (1-(1+beta)*init_weights[crit])/(1-init_weights[crit])
    new_weights = []
    for k in range(crits):
        if k == crit:
            new_weights.append(new_weight)
        else:
            new_weights.append(alpha*init_weights[k])

    return new_weights

def si_weights_update(walking_weights, init_weights, alternatives, criteria, func_pref_crit):
    EPS=1e-5
    si_weights = [[[],[]] for i in range(len(criteria))]
    si_rankings = [[[],[]] for i in range(len(criteria))]
    si_firsts =  [[[],[]] for i in range(len(criteria))]
    si_diffs =  [[[],[]] for i in range(len(criteria))]
    for k in range(len(criteria)):
        if walking_weights[k][0] != 0:
            si_weights[k][0] = weights_update(init_weights,walking_weights[k][0]-EPS,k)
            si_ranking = netflows_eval(alternatives,si_weights[k][0],func_pref_crit)
            ind = sorted(range(len(si_ranking)), key=lambda k: si_ranking[k], reverse=True)
            si_rankings[k][0] = ind
            si_firsts[k][0] = ind[0]
            si_diffs[k][0] = 2*abs(init_weights[k] - walking_weights[k][0])
            # print('--')
            # for i in ind:
            #     print(names[i])
        if walking_weights[k][1] != 1:
            si_weights[k][1] = weights_update(init_weights,walking_weights[k][1]+EPS,k)
            si_ranking = netflows_eval(alternatives,si_weights[k][1],func_pref_crit)
            ind = sorted(range(len(si_ranking)), key=lambda k: si_ranking[k], reverse=True)
            si_rankings[k][1] = ind
            si_firsts[k][1] = ind[0]
            si_diffs[k][1] = 2*abs(init_weights[k] - walking_weights[k][1])
            # print('--')
            # for i in ind:
            #     print(names[i])

    return si_weights, si_rankings, si_firsts, si_diffs

def paretoFilter(alternatives, criteria):
    altFilt = []
    for alt1 in alternatives:
        paretoFront = True
        for alt2 in alternatives:
            if alt1 == alt2:
                continue
            if paretoInf(alt1, alt2, criteria):
                paretoFront = False
                break
        if (paretoFront):
            altFilt.append(alt1)

    ind = []
    for alt in altFilt:
        ind.append(alternatives.index(alt))
    return altFilt, ind

def paretoInf(alt1, alt2, criteria):
    equals = 0
    for i in range(len(criteria)):
        valAlt1 = alt1[i]
        valAlt2 = alt2[i]
        if (valAlt1 > valAlt2):
            return False
        if (valAlt1 == valAlt2):
            equals = equals + 1
    return equals < len(criteria)
