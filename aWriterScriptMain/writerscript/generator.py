"""writerscript.generator module.
BrainFuck To Writer Script Converter with custom Text.

Copyright (c) 2020 Saket Upadhyay
"""
bf2ws_dir = {
    '+': 5,
    '-': 6,
    '[': 7,
    ']': 8,
    '>': 9,
    '<': 10,
    ',': 11,
    '.': 12
}

def bf2wsop(bfstr):
    opcodes=[]
    for i in bfstr:
        opcodes.append(bf2ws_dir[i])
    return opcodes

def GEN(BFsourceFile,TextSourceFile):

    bfc=""
    with open(BFsourceFile,'r') as bfcf:
        bfc=bfcf.readlines()[0].strip('\n')
    lims=bf2wsop(bfc)
    srcString=""
    sum=0
    for i in lims:
        sum+=i

    with open(TextSourceFile,'r') as src:
        sourcedat=list(src)[0].strip('\n')

    
    while(len(srcString)<sum):
        srcString=sourcedat.split(' ')
        sourcedat=sourcedat[len(srcString):-1]
    print("Source Feed : "+str(sum)+" Words Needed, "+str(len(srcString))+" Provided.")

    
    with open('out.pen','w') as dest:
        sptr=0
        dptr=0
        for lim in lims:
            dat=""
            dptr+=lim
            try:
                for i in range(sptr,dptr):
                        dat+=srcString[i]+' '
            except IndexError:
                print("Not Enough Source Feed : "+str(sum)+" Words Needed, "+str(len(srcString))+" Provided.")
                exit(-1)

            dat=dat[0:-1]
            dest.write(dat+','+'\n')
            sptr+=lim
    print("Done.")

        



