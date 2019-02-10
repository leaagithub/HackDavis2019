#Hackathon DNA Program 
import re

DNASeq = ''
SSR = ''
iteratorCount = 0
indexlist = []
insertionCount = 0
checkCount = 0 
zeroCount = 0 

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
    #print "list: " + line1
    line = SSR + ',' + str(iteratorCount) + ',' + line1 + '\n'
    f.write(line)

#END FUNCTIONS

DNASeq = getDNASeq();
writeHeader();
with open('SSRList.txt','r') as f:
    for line in f:
        line = str(line)
        #line = line.rstrip('\n')
        line = line.replace('\r',"")
        line = line.replace('\n',"")
        line = line.replace(' ',"")
        if line == "AT":
            #print 'works'
        #print line
        m = re.compile(line)
        #translates string into object
        for match in m.finditer(DNASeq):
            #print 'for loop check'
            #MATCHES SSR INTO DATA SEQUENCES AND INCREMENTS IF FOUND, GOES NEXT
            iteratorCount += 1
            #print match.span()
            l = list(match.span())
            #print l
            indexlist.append(l)
            #print indexes
        #print iteratorCount
        #print line
        #print indexlist
        if iteratorCount != 0:
            writeOutput(line,iteratorCount,indexlist)
            insertionCount += 1
            print 'SSR Found: ' ,insertionCount

        else:
            zeroCount += 1
            print '0 SSR Found. Zero Count: ', zeroCount

        iteratorCount = 0
        del indexlist[:]
        checkCount += 1
print "Done checking SSR List. Total SSR Checked: ",checkCount, "Total Found is: ",insertionCount