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
                if jse[0] + 1 == jse[1] - 1:
                    j = rl[jse[0] + 1]
                else:
                    j = joinLines(rl,jse[0] + 1,jse[1] - 1)
                # -----------
                if len(j) > 130:
                    desc = j[0:130] + "..."
                else:
                    desc = j
    return desc
if __name__ == '__main__':
    mySumm = summary(b"# ImgShare, now with Mobile!\nFree, easy image sharing using c9.io\n## About\nThis is a little server written in python that I wrote up in a day    \nthat allows you to upload images without any account, or fees.    \nThis server is made to run on [cloud 9](http://c9.io). This is a website    \nthat essentially allows you to remotely control an unbuntu machine.    \nAs a cherry on top, c9 gives you teporary hosting (domain name) for free.    \nThe idea of this project was quick, free and easy. However, c9 does have premium accounts (similar to github and other cloud platforms.)\n## Links\nMy c9 project : https://ide.c9.io/calderwhite/imgshare    \nWhen running, this is the upload domain: https://imgshare-calderwhite.c9users.io\n## Usage\n### Backend (Terminal)\nFrom the backend all there is to do is run the file.\n#### Execution\nTo run, enter the imgshare directory and then run:    \n`python3 c9Server.py`\n### Browser (Client)\nFrom a Browser you can upload, and view (download) images.\n#### Viewing\nIn order to view an image from a web page (when server running), here's how:    \n`https://imgshare-<username>.c9users.io/userData/userFiles/<user's ip>/<filename>`\n#### Uploading\nUploading is rather simple, just go to the base domain:    \n`https://imgshare-<username>/c9users.io`".decode('utf-8'))
    print(mySumm)
