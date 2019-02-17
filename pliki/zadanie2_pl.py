import sys
from collections import defaultdict

f_name=None
if len(sys.argv)>1:
    f_name=sys.argv[1]


def prepare_line(napis):
    login,akcja,czas=napis.split(";")
    czas=int(czas)
    return login, akcja, czas

if f_name:
    login_time = {}
    user_total_time = defaultdict(int)

    with open (f_name) as f:
        for line in f:
            login, akcja, czas =prepare_line(line)

            if akcja == "LOGIN":
                login_time[login]=czas
            elif akcja=="LOGOUT":
                session_time=int(czas)-int(login_time[login])
                user_total_time[login]+=session_time
    print("Czas przebywania w systemie: ")
    for login, czas in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
        print(f"{login}:{czas} s")


# jeśli chce posortować po userze od 1-10 (przy normalnym sortowaniu po userze byłoby 1, 10, 2, ...) zamieniam key=lambda itd na:
# key=my_key
# def my_key(item):
#     return int(item[0].split("-")[-1])

#print(login_time)
#print(user_total_time)








