import shutil
import os
import errno
from re import sub


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

def aBc(string):
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return string[0].lower() + string[1:]

def ABc(string):
    aBcRet = aBc(string)
    return aBcRet[0].upper() + aBcRet[1:]

def Abc(string):
    string = string.capitalize()
    return string

def nnn(string):
    return string

def Ann(string):
    return string[0].upper() + string[1:]

def inj(child,exprForHoleFncName,localExpr,targetExpr,separatorExpr=None):
    #print('inj localExpr: '+localExpr+' targetExpr: '+targetExpr)
    localExprOut = child.xpath(localExpr)
    #print('localExprOut:'+str(localExprOut))

    localExprOutLen = len(localExprOut)
    i=0
    mainFncOut=''
    while (i < localExprOutLen):
        strLocalExprOut = localExprOut[i]
        #print('i:'+str(i)+' strLocalExprOut:'+strLocalExprOut)

        #print('targetExpr:'+targetExpr)

        auxTargetExpr = targetExpr.replace('1',strLocalExprOut)

        #print('auxTargetExpr:'+auxTargetExpr)

        fncOut = child.xpath(auxTargetExpr)
        #print('fncOut:'+str(fncOut))
        #print('fncOut[0]:'+fncOut[0])

        #fnc = globals()[exprForHoleFncName]

        if isinstance(fncOut, list): 
            fncOut = fncOut[0]

        #fncOut = fnc(fncOut)

        if (separatorExpr != None):

            separatorExprOut = child.xpath(separatorExpr)

            if isinstance(separatorExprOut, list): 
                separatorExprOut = separatorExprOut[0]
            fncOut = fncOut + separatorExprOut

        #fncOut = fnc(fncOut)

        #mainFncOut = mainFncOut + fncOut

        if (exprForHoleFncName[-1] == '1'):
            fnc = globals()[exprForHoleFncName[:-1]]
            #print(fncOut)
            fncOut = fnc(fncOut)
            #print('fncOut: '+fncOut)

        mainFncOut = mainFncOut + fncOut

        i = i + 1

    #fnc = globals()[exprForHoleFncName]
    #print("calling..."+exprForHoleFncName)

    #if (exprForHoleFncName[-1] == '1'):
    #    fnc = globals()[exprForHoleFncName[:-1]]
    #    print(mainFncOut)
    #    mainFncOut = fnc(mainFncOut)
    

    if (separatorExpr != None):
        mainFncOut = mainFncOut[:-len(separatorExprOut)]

    return mainFncOut

def it(child,data):
    out = specialTransformationTarget
    i = 0
    strLen = len(specialTransformationTarget)
    while (i < strLen):
        pos = specialTransformationTarget.find(' >>>',i)
        if pos > -1:
            endPos = specialTransformationTarget.find('<<',pos)

            strToReplace = specialTransformationTarget[pos:endPos+2]
            exprForHole = specialTransformationTarget[pos+4:endPos]
            
            if "'" in exprForHole :
                lstExprForHole = exprForHole.split("'")

                exprForHoleFncName = lstExprForHole[0]
                exprForHoleXpathExpr = lstExprForHole[1]

                fncOut = child.xpath(exprForHoleXpathExpr)

                lstExprForHoleLen = len(lstExprForHole)
                if (lstExprForHoleLen >= 4):
                    exprForHoleXpathExpr2 = lstExprForHole[2]
                if (lstExprForHoleLen >= 5):
                    exprForHoleXpathExpr3 = lstExprForHole[3]
                    #print('5! '+exprForHoleXpathExpr3)
                
                if isinstance(fncOut, list): 
                    fncOut = fncOut[0]
                    
                if exprForHoleFncName != '':
                    #fnc = globals()[exprForHoleFncName]

                    try: exprForHoleXpathExpr2
                    except NameError:
                        #print("[it] calling exprForHoleFncName ..."+exprForHoleFncName)
                        #fncOut = fnc(fncOut)
                        pass
                    else:
                        #print('exprForHoleFncName:'+exprForHoleFncName)
                        #print('exprForHoleXpathExpr:'+exprForHoleXpathExpr)
                        #print('exprForHoleXpathExpr2:'+exprForHoleXpathExpr2)
                        
                        if (lstExprForHoleLen >= 4):
                            fncOut = inj(child,exprForHoleFncName,exprForHoleXpathExpr,exprForHoleXpathExpr2)
                        if (lstExprForHoleLen >= 5):
                            #print('exprForHoleXpathExpr3:'+exprForHoleXpathExpr3)
                            fncOut = inj(child,exprForHoleFncName,exprForHoleXpathExpr,exprForHoleXpathExpr2,exprForHoleXpathExpr3)
                        
                    #print("[it] calling exprForHoleFncName ..."+exprForHoleFncName)

                    if (exprForHoleFncName[-1] != '1'):
                        fnc = globals()[exprForHoleFncName]
                        fncOut = fnc(fncOut)

            else:
                if exprForHole != '':
                    fnc = globals()[exprForHole]
                    #print("[it] calling exprForHole ..."+exprForHole)
                    fncOut = fnc(data)
                else:
                    fncOut = data
            #print(fncOut)
            out = out.replace(strToReplace,fncOut)
            i = endPos
        else:
            i = i + 1

    return out

def i(xpathExpr,tag):
    parentStr = '' 
    for child in projectFileRoot.xpath(xpathExpr):
        childStr = ''
        for subChild in child:
            if subChild.tag == tag:
                childStr = it(child,subChild.text)
                parentStr = parentStr + childStr
    return parentStr

def resolveSpecialTransformation():
    global specialTransformationFlag 
    specialTransformationFlag = 'end'
    fnc = globals()[fncName]
    fncOut = fnc(fncPar,end)

    return fncOut

def setSpecialTransformation(line):
    global specialTransformationFlag 
    specialTransformationFlag = 'copy'

    global fncName
    global fncPar
    global end

    stPos = line.find('<<<')
    fncNamePos = stPos + 3
    stEndPos = line.find('>>',fncNamePos)
    st = line[fncNamePos:stEndPos]
    par = st.split("'")
    fncName = par[0]
    fncPar = par[1]
    end = par[2]

def parse(line,mode=None):
    start = '<'
    end = '>'

    if mode != None:
        if 'xml' in mode:
            start = ''
            end = ''
    
    line = line.replace(start + "*e" + end, projectFileRoot.findall('./entity')[0].text)
    line = line.replace(start + "*E" + end, projectFileRoot.findall('./entity')[0].text.capitalize())
    line = line.replace(start + '*EE' + end, projectFileRoot.findall('./entity')[0].text.upper())
    line = line.replace(start + '*pkField' + end, projectFileRoot.findall('./pkField')[0].text)
    line = line.replace(start + '*table' + end, projectFileRoot.findall('./table')[0].text)
    line = line.replace(start + '*entityFancyTextName' + end, projectFileRoot.findall('./entityFancyTextName')[0].text)
    
    if '<<<>' in line:
        return resolveSpecialTransformation()
    else:
        if ( start + '<<' ) in line:
            setSpecialTransformation(line) 
            return ''
        else:
            return line

def parseCopyInternal(srcobj, dstname):
    global specialTransformationFlag
    specialTransformationFlag = ''

    global specialTransformationTarget
    specialTransformationTarget = ''
    if "*" in dstname:
        dstname = parse(dstname,'xml')

    with open(srcobj, 'rt') as fin:
        with open(dstname, 'wt') as fout:
            for line in fin:
                #print('parsing...')
                parseOut = parse(line)

                if specialTransformationFlag == '':
                    fout.write(parseOut)
                else:
                    if specialTransformationFlag == 'copy':
                        specialTransformationFlag = 'start'
                    else:
                        if specialTransformationFlag == 'start':
                            specialTransformationTarget = specialTransformationTarget + line
                        else:
                            if specialTransformationFlag == 'end':
                                fout.write(parseOut)
                                specialTransformationFlag = ''
                                specialTransformationTarget = ''


def parseCopy(localProjectFileRoot,skeletorPath,fileText,projectNameDstPath):
    global projectFileRoot 
    projectFileRoot = localProjectFileRoot

    skeletorBasePath = 'skeletor'
    try:
        srcDirname = os.path.dirname(os.path.join(skeletorBasePath,skeletorPath,fileText))

        dstDirname = os.path.dirname(os.path.join('outs',projectNameDstPath,skeletorPath,fileText))
        
        #dstDirname = dstDirname.replace('*', projectFileRoot.findall("./entity")[0].text)
        if '*' in dstDirname:
            dstDirname = parse(dstDirname,'xml')
            
        shutil.copytree(srcDirname,dstDirname,copy_function = parseCopyInternal)
    except OSError as e:
        if e.errno == errno.EEXIST:
            #file exist!
            pass
        else:
            raise
