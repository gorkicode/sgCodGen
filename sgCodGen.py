#!/usr/bin/python3

#	Sioft Code Generator in Python (sgCodGen)
#
#	Gorkicode

import sys, getopt
import os
#import xml.etree.ElementTree as ET
import lxml.etree as ET
import importlib

TITLE = 'Sioft Code Generator in Python (sgCodGen) 13/07/2018'
VERSION = '0.1.0-alpha.1'
FIRM = 'Gorkicode'
USAGE = 'python sgCodGen.py --projectFileName <projectFile NameInProjectsFolderWithOut.Xml>'

def parseXmlProjectFile(projectFilePath):
    projectFileTree = ET.parse(projectFilePath)
    projectFileRoot = projectFileTree.getroot()
    projectName = projectFileRoot.findall('./name')
    projectNameDstPath = projectName[0].text
    for skeletor in projectFileRoot.findall('./skeletors/skeletor'):
        for name in skeletor.findall('./name'):
            skeletorPath = name.text
            skeletorModule = importlib.import_module('skeletor'+'.'+skeletorPath+'.'+'skeletor')
        for file in skeletor.findall('./transformation/file'):
            if '**' in file.text:
                #special transformation
                pass
            else:
                skeletorModule.parseCopy(projectFileRoot,skeletorPath,file.text,projectNameDstPath)

def displayVersionHelpAndExit():
    print(TITLE + '\n' + BUILD_VER + '\n' + FIRM + '\n\n' + USAGE + '\n')
    sys.exit(2)

def readArgv(argv):
    projectFileName = ''
    
    try:
        opts, args = getopt.getopt(argv,'',['projectFileName='])
    except getopt.GetoptError:
        displayVersionHelpAndExit()

    for opt, arg in opts:
        if opt in ('--projectFileName'):
            projectFileName = arg

    return projectFileName

def main(argv):
    projectFileName = readArgv(argv)

    if not projectFileName :
        displayVersionHelpAndExit()

    ext = '.xml'
    projectFilePath = os.path.join(os.getcwd(), 'projects', projectFileName + ext)

    parseXmlProjectFile(projectFilePath)

if __name__ == '__main__':
    main(sys.argv[1:])