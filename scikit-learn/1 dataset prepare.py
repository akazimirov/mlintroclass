#Dataset URL: https://archive.ics.uci.edu/ml/datasets/spambase
f = open("spambase.data", "r")
ftrain = open("spambase.train", "w")
ftest = open("spambase.test", "w")
fnew = open("spambase", "w")
count = 0
test = 0
train = 0
for line in f:
    count += 1
    fnew.write(line)
    if count % 10 == 0:
        ftest.write(line)
        test += 1
    else:
        ftrain.write(line)
        train += 1
    

ftrain.close()
ftest.close()
f.close()
fnew.close()
print(count, test, train)
