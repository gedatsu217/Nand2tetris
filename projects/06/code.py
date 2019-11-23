class Code:
    def dest(self, char):
        if(char=="null"):
            return "000"
        elif(char=="M"):
            return "001"
        elif(char=="D"):
            return "010"
        elif(char=="MD"):
            return "011"
        elif(char=="A"):
            return "100"
        elif(char=="AM"):
            return "101"
        elif(char=="AD"):
            return "110"
        elif(char=="AMD"):
            return "111"

    def comp(self, char):
        if("M" in char):
            ans="1"
        else:
            ans="0"
        if(char=="0"):
            ans += "101010"
        elif(char=="1"):
            ans += "111111"
        elif(char=="-1"):
            ans += "111010"
        elif(char=="D"):
            ans += "001100"
        elif(char=="A" or char=="M"):
            ans += "110000"
        elif(char=="!D"):
            ans += "001101"
        elif(char=="!A" or char=="!M"):
            ans += "110001"
        elif(char=="-D"):
            ans += "001111"
        elif(char=="-A" or char=="-M"):
            ans += "110011"
        elif(char=="D+1"):
            ans += "011111"
        elif(char=="A+1" or char=="M+1"):
            ans += "110111"
        elif(char=="D-1"):
            ans += "001110"
        elif(char=="A-1" or char=="M-1"):
            ans += "110010"
        elif(char=="D+A" or char=="D+M"):
            ans += "000010"
        elif(char=="D-A" or char=="D-M"):
            ans += "010011"
        elif(char=="A-D" or char=="M-D"):
            ans += "000111"
        elif(char=="D&A" or char=="D&M"):
            ans += "000000"
        elif(char=="D|A" or char=="D|M"):
            ans += "010101"

        return ans

    def jump(self, char):
        if(char=="null"):
            return "000"
        elif(char=="JGT"):
            return "001"
        elif(char=="JEQ"):
            return "010"
        elif(char=="JGE"):
            return "011"
        elif(char=="JLT"):
            return "100"
        elif(char=="JNE"):
            return "101"
        elif(char=="JLE"):
            return "110"
        elif(char=="JMP"):
            return "111"