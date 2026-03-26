# Value Iteration Algorithm Package

## The Package

This package contains code to carry out the value iteration algorithm for computing the optimal policy for an MDP and the asscoiated value. This package contains the python script with the value iteration function. It additioanlly conatins two examples, in the form of jupyter notebook files where each example is laid out and solved. Finally, there are also a few unit tests.

## How to Use the Package

To install the package using the unix console type:

python -m pip install 'git+https://github.com/jstrong12/STOR609_CW2'

## The Value Iteration Algorithm

### Input

S = Set of States \
A = Set of Actions \
P = State Transition Function P(s'|s,a) \
R = Reward Function R(s,a) or R(s'|s,a) \
$\gamma$ = Discount Factor\
$\epsilon$ = Convergence Parameter\
Mode = 1 if R is of the form R(s,a) or 2 if R is of the form R(s'|s,a) 

### Output

V = Value Function \
$\pi$ = Optimal Policy

### Pseudocode

```text
Value_iteration(S,A,P,R,γ,ε,mode):
    n1 = Length of S
    n2 = Length of A 
    V = List of n1 zeros
    π = List of n2 zeros
    Diff = 1 
    k = 0

    if mode = 1:
        while Diff > ε:
            k = k + 1
            Vold = V
            for each state s:
                V[s] = max_a [R(s,a) + γ * sum_{s'} (P(s'|s,a) * Vold[s'])]
            Diff = max_s (|V[s] - Vold[s]|)

        for each state s:
            π[s] = max_a [R(s,a) + γ * sum_{s'} (P(s'|s,a) * Vold[s'])]
        return π, V

    if mode = 2:
        while Diff > ε:
            k = k + 1
            Vold = V
            for each state s:
                V[s] = max_a [sum_{s'} (P(s'|s,a) * (Vold[s'] * γ + R(s'|s,a)))]
            Diff = max_s (|V[s] - Vold[s]|)

        for each state s:
            π[s] = max_a [sum_{s'} (P(s'|s,a) * (Vold[s'] * γ + R(s'|s,a)))]
        return π, V
```

## How This Code Compares to Figure 9.16

Figure 9.16 provides pseudocode for the value iteration algorithm, though it is not too specific on some aspects. For example, it says to run a repeat loop until termination, but does not really mention what this actually means. While in my code we run a while loop until we reach convergence as defined by whether the maximum absolute value of the difference between our V and the prior V for each state is less than epsilon. This is one of the main differences, that my code takes gamma and epsilon as an input, while theirs does not. Their code and Q function are defined for the case where we have R(s,a), thus all the formulas in mode one of my code match the code in 9.16. This is fine for our Sam Weekend example, but is not enough for the Grid World Problem, which has a R(s'|s,a) style reward function. Therefore, I needed to find a different Q function for problems of that style which can be found in mode 2. The two functions can be found below:

$$
\text{Mode 1:} \quad V[s] = \max_a (\text{R(s,a)} + \gamma * \Sigma_{s'} (\text{P(s'|s,a) * Vold\[s'\]})) \quad \text{(Matches 9.16)}
$$

$$
\text{Mode 2:} \quad V[s] = \max_a (\Sigma_{s'} (\text{P(s'|s,a) * (Vold\[s'\]} * \gamma + \text{R(s'|s,a)})))
$$

Realistically I think I could have just used the Q function from Mode 2, but the task was to try and recreate the code from 9.16, so I thought it would be good to have both cases. The final difference I can spot is that I am pretty sure they are storing the values of V for all k, where my code only uses the current V and the one prior, defined as Vold. I am not one hundred percent sure if this is what they are doing though, as their pseudocode leaves a lot to interpretation.
