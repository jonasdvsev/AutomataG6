
def Regex1checkString(conv):
    print("regex1")
    state_list = []
    state_list.append("s0")
    state = 0
    for x in range(0, len(conv)):
        if x == 0:
            if conv[x: x + 1] == "a":
                print("show state 3 pic")
                state = 3
                state_list.append("s3")
            elif conv[x: x + 1] == "b":
                print("show state 1 pic")
                state = 1
                state_list.append("s1")

        elif x == 1:
            if state == 3:
                if conv[x: x + 1] == "a":
                    print("show state TRAP pic")
                    state_list.append("st")
                    break
                elif conv[x: x + 1] == "b":
                    print("show state 4 pic")
                    state = 4
                    state_list.append("s4")
            elif state == 1:
                if conv[x: x + 1] == "a":
                    print("show state 2 pic")
                    state = 2
                    state_list.append("s2")
                elif conv[x: x + 1] == "b":
                    print("show state TRAB pic")
                    state_list.append("st")
                    break

        elif x == 2:
            if state == 4:
                if conv[x: x + 1] == "b":
                    print("show state TRAP pic")
                    state_list.append("st")
                    break
                elif conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
            elif state == 2:
                if conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "a":
                    print("show state TRAB pic")
                    state_list.append("st")
                    break

        elif x == 3:
            if conv[x: x + 1] == "a":
                print("show state 5 pic")
                state = 5
                state_list.append("s5")
            elif conv[x: x + 1] == "b":
                print("show state 6 pic")
                state = 6
                state_list.append("s6")

        elif x == 4:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

        elif x == 5:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

        elif x == 6:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 7:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 8:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 9:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 10:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 11:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 12:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")

        elif x == 13:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
        elif x == 14:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
        elif x == 15:
            if state == 5:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 6 pic")
                    state = 6
                    state_list.append("s6")
            elif state == 6:
                if conv[x: x + 1] == "a":
                    print("show state 7 pic")
                    state = 7
                    state_list.append("s7")
                elif conv[x: x + 1] == "b":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")

            elif state == 7:
                if conv[x: x + 1] == "a":
                    print("show state 5 pic")
                    state = 5
                    state_list.append("s5")
                elif conv[x: x + 1] == "b":
                    print("show state 8 pic")
                    state = 8
                    state_list.append("s8")

            elif state == 8:
                if conv[x: x + 1] == "a":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
                elif conv[x: x + 1] == "b":
                    print("show state END pic")
                    state = 9
                    state_list.append("s9")
    return state_list


