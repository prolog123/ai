def water_jug_problem(jug1,jug2, target):
    jug1_level, jug2_level = 0,0
    step=0
    while jug1_level != target and jug2_level != target:
        if jug1_level ==0:
            jug1_level = jug1
        elif jug2_level == jug2:
            jug2_level =0
        elif jug1_level>0 and jug2_level<jug2:
            amount = min(jug1_level,jug2-jug2_level)
            jug1_level -= amount
            jug2_level += amount
        elif jug2_level>0 and jug1_level<jug1:
            amount= min(jug2_level,jug1-jug1_level)
            jug1_level+= amount
            jug2_level -= amount
        else:
            jug1_level =0
        step +=1

        print(jug1_level,jug2_level)
    print("steps: ",step)

water_jug_problem(4,3,2)
