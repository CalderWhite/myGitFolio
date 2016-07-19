import ghAuth, json, base64, summarize_v2, sys
import urllib.request as request

def get_sorted_repos(token,order="date",private=True):
    repoUrl = "https://api.github.com/user/repos?access_token=" + token + "&visibility="
    public = request.urlopen(repoUrl + "public")
    repos = []
    if private:
        allRepo = request.urlopen(repoUrl + "all")
        repoAll = json.loads(allRepo.read().decode('utf-8'))
        repos = repoAll
    else:
        repoPu = json.loads(public.read().decode('utf-8'))
        for i in repoPu:
            repos.append(i)
    if len(repos) < 1:
        # no repos to gather!
        raise Exception
    if order == "date":
        repos.sort(key=lambda r: r["created_at"],reverse=True)
        # you have to revese the sort, since by default it sorts oldest to newest
    elif order == "stars":
        repos.sort(key=lambda r: r["stargazers_count"],reverse=True)
    elif order == "watchers":
        repos.sort(key=lambda r: r["watchers_count"])
    else:
        # no known order string was passed in
        raise Exception
    return repos

def build_summary(repoUrl,token,repoJson):
    err = False
    try:
        global readme_req
        global readme
        readme_req = request.urlopen(repoUrl + "/readme?access_token=" + token)
        readme = readme_req.read()
    except:
        print("ERROR: got code " + str(readme_req.getcode()))
        # too lazy to check for other errors, or to make sure the object is in fact the correct one -_-
        global err
        err = True
    if err:
        decoded_contents = None
    else:
        readme = json.loads(readme.decode('utf-8'))
        ending = readme["name"].split(".")[-1]
        if ending.lower() != "md":
            decoded_contents = False
            print("ERROR: bad file type: " + ending)
        else:
            b64encoded_contents = readme["content"]
            encoded_contents = base64.b64decode(b64encoded_contents)
            #encoded_contents = str(encoded_contents)[2:len(str(encoded_contents)) - 1]
            decoded_contents = encoded_contents.decode('utf-8')
    summary = summarize_v2.summary(decoded_contents,repoJson)
    return summary
def buildFile(ftype,oauth_token,myOrder="date",privateRepos=True):
    print("retrieving repositories...")
    repoList = get_sorted_repos(oauth_token,order=myOrder,private=privateRepos)
    summaries = []
    print("building summaries...")
    for i in repoList:
        x = build_summary(i["url"],oauth_token,i)
        summaries.append([x,i["name"]])
        print("summary " + str(repoList.index(i)) + " is complete.")
    print(summaries)

if __name__ == '__main__':
    print("authenticating....")
    r = open("userData.json",'r')
    rj = json.loads(r.read())
    r.close()
    if rj.__contains__("oauth_token"):
        oauth_token = rj["oauth_token"]
    else:
        oauth_token = ghAuth.getAuth()
        jBuild = {}
        jBuild["oauth_token"] = oauth_token
        jstr = json.dumps(jBuild,indent=4)
        w = open("userData.json", 'w')
        w.write(jstr)
        w.close()
        print("--------------")
    buildFile("bruh",oauth_token)
