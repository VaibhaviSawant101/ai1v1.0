import sys

start_state = []
goal_state = []
current_state = []
planning_stack = []
actual_plan = []

actions = ["stack", "unstack", "pickup", "putdown"]
predicates = ["on", "clear", "arm_empty", "holding", "on_table"]


def preconditions_stack(X, Y):
    planning_stack.append("holding "+str(X))
    planning_stack.append("clear "+str(Y))


def preconditions_unstack(X, Y):
    planning_stack.append("on "+str(X)+" "+str(Y))
    planning_stack.append("clear "+str(X))


def preconditions_pickup(X):
    planning_stack.append("arm_empty")
    planning_stack.append("on_table "+str(X))
    planning_stack.append("clear "+str(X))


def preconditions_putdown(X):
    planning_stack.append("holding "+str(X))


def for_on(X, Y):
    planning_stack.append("stack "+str(X)+" "+str(Y))
    preconditions_stack(X, Y)


def for_ontable(X):
    planning_stack.append("putdown "+str(X))
    preconditions_putdown(X)


def for_clear(X):

    check = "on "

    for predicate in current_state:
        if check in predicate:
            temp_list = predicate.split()

            if temp_list[2] == X:
                break

    Y = str(temp_list[1])

    planning_stack.append("unstack "+str(Y)+" "+str(X))
    preconditions_unstack(Y, X)


def for_holding(X):
    check = "on_table "+str(X)

    if check in current_state:
        planning_stack.append("pickup "+str(X))
        preconditions_pickup(X)

    else:
        check = "on "

        for predicate in current_state:
            if check in predicate:
                temp_list = predicate.split()

                if temp_list[2] == X:
                    break

        Y = str(temp_list[1])

        planning_stack.append("unstack "+str(Y)+" "+str(X))
        preconditions_unstack(Y, X)


def for_armempty():
    print("\nArm empty predicate false\n")
    sys.exit()
    # This function is used to exit from either the Python console or command prompt, and also used to exit from the program in case of an exception.


def effect_stack(X, Y):
    current_state.remove("holding "+str(X))
    current_state.remove("clear "+str(Y))

    current_state.append("on "+str(X)+" "+str(Y))
    current_state.append("clear "+str(X))
    current_state.append("arm_empty")


def effect_unstack(X, Y):
    current_state.remove("on "+str(X)+" "+str(Y))
    current_state.remove("clear "+str(X))
    current_state.remove("arm_empty")

    current_state.append("holding "+str(X))
    current_state.append("clear "+str(Y))


def effect_pickup(X):
    current_state.remove("arm_empty")
    current_state.remove("on_table "+str(X))
    current_state.remove("clear "+str(X))

    current_state.append("holding "+str(X))


def effect_putdown(X):
    current_state.remove("holding "+str(X))

    current_state.append("arm_empty")
    current_state.append("on_table "+str(X))
    current_state.append("clear "+str(X))


input_string = input("Enter start state:- ")
start_state = input_string.split("^")

input_string = input("Enter goal state:- ")
goal_state = input_string.split("^")

print("\nEntered Start State:- "+str(start_state))
print("\nEntered Goal State:- "+str(goal_state)+"\n")

current_state = start_state.copy()

for predicate in goal_state:
    planning_stack.append(predicate)

while len(planning_stack) > 0:
    print("Planning Stack:- "+str(planning_stack))
    print("Current State:- "+str(current_state)+"\n")

    top = planning_stack.pop()
    temp = top.split()

    if temp[0] in predicates:

        if top in current_state:
            continue

        else:

            if temp[0] == "on":
                for_on(temp[1], temp[2])
            elif temp[0] == "on_table":
                for_ontable(temp[1])
            elif temp[0] == "clear":
                for_clear(temp[1])
            elif temp[0] == "holding":
                for_holding(temp[1])
            elif temp[0] == "arm_empty":
                for_armempty()

    if temp[0] in actions:

        if temp[0] == "stack":
            effect_stack(temp[1], temp[2])
        elif temp[0] == "unstack":
            effect_unstack(temp[1], temp[2])
        elif temp[0] == "pickup":
            effect_pickup(temp[1])
        elif temp[0] == "putdown":
            effect_putdown(temp[1])

        actual_plan.append(top)

print("Final Current State:- "+str(current_state))

print("\nPlan Generated:- \n")
for step in actual_plan:
    print(step)

# input :
# Start state : on B A^on_table A^clear B^arm_empty
# goal state : on A B^on_table B^clear A^arm_empty


# Algorithm:

# Push the Goal state in to the Stack

# Push the individual Predicates of the Goal State into the Stack

# Loop till the Stack is empty

# Pop an element E from the stack

# IF E is a Predicate

# IF E is True then

# Do Nothing

# Advertisements

# REPORT THIS AD

# ELSE

# Push the relevant action into the Stack

# Push the individual predicates of the Precondition of the action into the Stack

# Else IF E is an Action

# Apply the action to the current State.

# Add the action ‘a’ to the plan
