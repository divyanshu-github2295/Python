import re
s = "11:50:00PM"
while True:
    if re.search("^0[0-9]|1[0-2]:[0-5][0-9]:[0-5][0-9][AP]M$", s):
        if s[8:] == "PM":
            if s[:2] != "12":
                print(str(int(s[:2])+12) + s[2:8])
                break
        elif s[8:] == "AM":
            if s[:2] == "12":
                print("00" + s[2:8])
                break
    print(s[:8])
    break
