import sys
import re
import os

A_COMMAND=0
C_COMMAND=1
L_COMMAND=2

class Parser:
    def initial(self):
        args=sys.argv
        if(len(args)!=2):
            print("args error")
            exit(1)
        

        if not(".asm" in args[1]):
            print("asm error")
            exit(1)
        

        self.file=open(args[1], 'r')
        self.export_file=open(args[1][:-4]+"1.hack", "w")

    def hasMoreCommands(self):
        self.line=self.file.readline()
        if(self.line):
            self.line=self.line.strip()
            return True

        else:
            return False
    
    
    def advance(self):
        while(1):
            if(self.line[:2]=="//" or self.line=='\n'):
                self.line=self.file.readline()
                continue
            elif(self.line):
                self.line=self.line.strip()
                break

    def commandType(self):
        if(self.line[0]=='@'):
            return A_COMMAND
        elif(self.line[0]=='('):
            return L_COMMAND
        else:
            return C_COMMAND

    def symbol(self):
        if(self.commandType()==A_COMMAND):
            return self.line[1:]
        elif(self.commandType()==L_COMMAND):
            return self.line[1:][:1]

    def dest(self):
        if('=' in self.line):
            line_list=re.split('[=;]', self.line)
            return line_list[0]

        else:
            return "null"

    def comp(self):
        line_list=re.split('[=;]', self.line)
        if("=" in self.line):
            return line_list[1]

        else:
            return line_list[0]

    def jump(self):
        line_list=re.split('[=;]', self.line)
        if(";" in self.line):
            return line_list[-1]

        else:
            return "null"

    def write(self, char):
        self.export_file.write(char+'\n')

    def finish(self):
        self.file.close()
        self.export_file.close()






