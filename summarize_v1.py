def joinLines(arr,st,en):
    res = []

    for i in range(st,en):
        res.append(arr[i])
    res = "\n".join(res)
    return res
def summary(text):
    desc = "Error loading description."

    if text == None or text == "":
        desc = "No description available."
    elif text.find("#") < 0:
        if len(text) > 130:
            desc = text[0:130] + "..."
        else:
            desc = text
    else:
        # don't just search for '#'s since it's less thorough
        rl = text.split("\n")
        if rl[-1] == "":
            rl.pop(-1)
        # get rid of the empty list item created by newline @ end of file
        jse = []
        for i in rl:
            if i != "":
                if i[0].find("#") > -1 or i[0].find("#") > -1:
                    jse.append(rl.index(i))
                if len(jse) >= 2:
                    break
        if len(jse) == 1:
            if jse[0] != 0:
                j = joinLines(rl,0,jse[0])
            else:
                if len(rl) == 2:
                    j = rl[1]
                else:
                    j = joinLines(rl,1,len(jse))
            if len(j) > 130:
                desc = j[0:130] + "..."
            else:
                desc = j
        elif len(jse) == 2:
            lines = jse[1] - jse[0]
            if lines == 0:
                # so it will return no description available
                pass
            elif lines == 1:
                # I might impliment a better algorithm for this situation later.
                pass
            else:
                j = joinLines(rl,jse[0] + 1,jse[1] - 1)
                if len(j) > 130:
                    desc = j[0:130] + "..."
                else:
                    desc = j
        print("[\n" + text + "\n]")
        print(jse)
        print("--------------------")
    return desc
if __name__ == '__main__':
    mySumm = summary("# Repo2\nThe second of my legendary github repositories!!!\n")
    print(mySumm)
