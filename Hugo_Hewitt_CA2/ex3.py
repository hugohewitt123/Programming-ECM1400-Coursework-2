"""This module chooses names from an input list and adds them to a team"""
def five_a_side_selector(names):
    '''This function selects names and assigns them to teams, in lists'''
    teams = round((len(names))/5)
    if teams == 1:
        teams+=1
    elif len(names) == 11 or len(names) == 12:
        teams += 1
    j = 0
    i = 0
    team = []
    while j < teams:
        temp = []
        loop = i
        while loop < len(names):
            temp.append(names[loop])
            loop+=teams
        team.append(temp)
        i+=1
        j+=1
    result = team
    return result

print( five_a_side_selector(["David", "Ronaldo", "Matthew", "Jacq", "Johan", "Achim"]) )
