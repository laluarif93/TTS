from subprocess import check_output
import time

xa,xb,xc,xd = [],[],[],[]


PATH = open("/usr/src/app/corpus_rev_3.txt","r")

for i in PATH:

    if len(i) <40:
        if len(xa) > 499:
            pass
        else :
            st = time.time()
            check_output(["espeak", "-vid", i])
            end = time.time()
            tm = end - st
            xa.append(tm)
    elif len(i) >=40 and len(i)<80:
        if len(xb) > 499:
            pass
        else :
            st = time.time()
            check_output(["espeak", "-vid", i])
            end = time.time()
            tm = end - st
            xb.append(tm)

    elif len(i) >=80 and len(i)<120:
        if len(xc) > 499:
            pass
        else :
            st = time.time()
            check_output(["espeak", "-vid", i])
            end = time.time()
            tm = end - st
            xc.append(tm)
    elif len(i) >=120 and len(i)<160:
        if len(xd) > 499:
            pass
        else:
            st = time.time()
            check_output(["espeak", "-vid", i])
            end = time.time()
            tm = end - st
            xd.append(tm)

    elif xa > 499 and xb > 499 and xc > 499 and xd > 499:
        break

print("waktu eksekusi [0-39 char] (s)", sum(xa)/len(xa))
print("waktu eksekusi [40-79 char] (s)",sum(xb)/len(xb))
print("waktu eksekusi [80-119 char] (s)",sum(xc)/len(xc))
print("waktu eksekusi [120-159 char] (s)",sum(xd)/len(xd))


