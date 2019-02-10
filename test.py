#Hackathon DNA Program 
import re

DNASeq = ''
SSR = 'AT'
iteratorCount = 0
indexlist = []

def getDNASeq():
    f = open('DNASeqList.txt', 'r')
    DNASeq = f.readline()
    print "DNA Sequence List is: " ,DNASeq
    return DNASeq
def writeHeader():
    f = open('output.txt', 'w')
    header = 'SSR,Count, indexes \n'
    f.writelines(header)
def writeOutput(SSR,iteratorCount,indexlist):
    line1 = ''
    f = open('output.txt', 'a')
    for x in indexlist:
        str1 = ','.join(str(e) for e in x)
        line1 = line1 + "|" +  str1
    print "list: " + line1
    line = SSR + ',' + str(iteratorCount) + ',' + line1 + '\n'
    f.write(line)
#END FUNCTIONS

DNASeq = getDNASeq();
writeHeader();
m = re.compile(SSR)
print m
#translates string into object
iterator = m.finditer(DNASeq)
for match in iterator:
    iteratorCount += 1
    #print match.span()
    l = list(match.span())
    #print l
    indexlist.append(l)
#print indexes
print iteratorCount
print SSR
print indexlist
writeOutput(SSR,iteratorCount,indexlist)
