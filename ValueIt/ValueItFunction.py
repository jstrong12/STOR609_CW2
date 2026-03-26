# S = State Set
# A = Action Set
# P = State Transition Function 
# R = Reward Function
# gamma = Discount Factor
# epsilon = Convergence Parameter
# mode = 1 if the reward function takes s and a, mode 2 if the reward function takes s',s and a 

def Value_iteration(S, A, P, R, gamma, epsilon, mode):
    l = len(S) #Find length of state set
    la = len(A) #Find length of action set
    V = [0] * l #Create initial vector of values
    Pi = [0] * l #Create initial vector of optimal policy
    Diff = 1 + epsilon #Create arbitary initial difference to start while loop
    k = 0 #Initialise the steps
    if mode == 1:
        while Diff > epsilon: #Keep running until convergence
            k = k + 1 #Update step counter
            Vold = V.copy() #Create a copy of our current values
            for i in range(l): #Run over all states
                t = []
                for j in range(la): #Run over all actions
                    s = S[i] #Select the state
                    a = A[j] #Select the action
                    m = 0 #Initialise the count for the summation
                    for k2 in range(l): #Run over all states but for s' this time to do summation
                        s2 = S[k2] #Select s'
                        v = P(s2, s, a) * Vold[k2] #Work out within sum value
                        m = m + v #Add to count
                    z = R(s2,s,a) + gamma * m #Work out value for action a
                    t.append(z)   #Add it to a list of values for all a
                zz = max(t) #Pick the maximum value maximum
                V[i] = zz #Update value for state
            Diffy = []
            for g in range(l): #Loop to find maximum distance between old values and new
                gg = abs(V[g] - Vold[g])
                Diffy.append(gg)
            Diff = max(Diffy) #Set Diff to maxiumum absolute distance between old values and new
        for i in range(l): #Now we have our final V, we do a similar loop to find the optimal policy
            t2 = []
            for j in range(la):
                s = S[i]
                a = A[j]
                m = 0
                for k2 in range(l):
                    s2 = S[k2]
                    v = P(s2, s, a) * V[k2]
                    m = m + v
                z = R(s2,s,a) + gamma * m
                t2.append(z)  
            zz = t2.index(max(t2))
            Pi[i] = A[zz]
        return [Pi, V] #Returns optimal policy and values
    
    if mode == 2: #Essentially does the exact same thing with a slight difference to how V and Pi is calculated
        while Diff > epsilon:
            k = k + 1
            Vold = V.copy()
            for i in range(l):
                t = []
                for j in range(la):
                    s = S[i]
                    a = A[j]
                    m = 0
                    for k2 in range(l): #Uses alternative formula
                        s2 = S[k2]
                        v = P(s2, s, a) * (Vold[k2] * gamma + R(s2,s,a))
                        m = m + v
                    t.append(m)  
                zz = max(t)
                V[i] = zz
            Diffy = []
            for g in range(l):
                gg = abs(V[g] - Vold[g])
                Diffy.append(gg)
            Diff = max(Diffy)
        for i in range(l):
            t2 = []
            for j in range(la):
                s = S[i]
                a = A[j]
                m = 0
                for k2 in range(l):
                    s2 = S[k2]
                    v = P(s2, s, a) * (Vold[k2] * gamma + R(s2,s,a))
                    m = m + v
                t2.append(m)  
            zz = t2.index(max(t2))
            Pi[i] = A[zz]
        return [Pi, V]
