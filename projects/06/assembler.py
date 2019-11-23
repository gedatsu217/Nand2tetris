from parser import Parser 
from code import Code

parser=Parser()
code=Code()

def main():
    parser.initial()
    while(1):
        if not(parser.hasMoreCommands()):
            break
        export=""
        parser.advance()
        command_type=parser.commandType()
        if(command_type==0 or command_type==2):
            command_symbol=int(parser.symbol())
            #print("symbol: "+command_symbol)
            binary_type02=format(command_symbol, 'b')
            length_type02=len(binary_type02)
            for _ in range(16-length_type02):
                export += "0"
            export += binary_type02
        elif(command_type==1):
            command_dest=parser.dest()
            command_comp=parser.comp()
            command_jump=parser.jump()

            code_dest=code.dest(command_dest)
            code_comp=code.comp(command_comp)
            code_jump=code.jump(command_jump)

            export += "111"+code_comp+code_dest+code_jump
            
            #print("dest: "+command_dest)
            #print("comp: "+command_comp)
            #print("jump: "+command_jump)

        parser.write(export)

    parser.finish()
    



if __name__ == '__main__':
    main()