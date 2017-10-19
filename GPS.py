#gps

def gps(initStates, goalStates, operators):
    #track which opperators have been applied
    #use a prefix

    prefix = 'Execute'
    for opperator in opperators:
        operator['add'].append(prefix + operator['action'])

    finalStates = achieveAll(initStates, goalStates, operators, [])

    if not finalStates:
        return None

    #only return what is being excecuted

    return[state for state in finalStates if state.startswith(prefix)]

def achieveAll(states, ops, goals, goalStack):
    #states = current states
    #ops = operators avialable
    # goals = goals to achive
    # goal stack = goals we've already started to achive

    #try to achive each of the goals in the order given.
    #if they're unachiavable, then it can't be solved

    for goal in goals:
        states = achieve(states, ops, goals, goalStack)
        if not states:
            return None #(can't be solved)

    #"prerequistite clobbers sibling goal problem"
    #dont remove other goals in the process of solving a different one

    for goal in goals:
        if goal not in states:
            return None
    
     return states


def achieve(states, ops, goal, goalStack):
    #args are the same, takes one goal

    #call applied ops
    if goal in states:
        return states

    #prevent going in circles
    if goal in goalStack:
        return None

    for op in ops:
        #is operator appropriate?
        if goal not in op['add']:
            continue
        #does it work
        result = applyOperator(op, states, ops, goal, goalStack)
        if result: # hey it worked!
            return result


def applyOperator(operator, states, ops, goal, goalStack):
    result = achiveALl(states, ops, operator['preconds'], goal + goalStack)
    if not results:
        return None # failed

    addList, deleteList = operator['add'], operator['delete']
    #update the current states by the removing the states

    return [state for state in result if state not in deleteList] + addList





        
        

    
    
    
        
    
    
