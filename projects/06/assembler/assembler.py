from parser import Parser 
from code import Code
from symboltable import SymbolTable


code=Code()
symboltable=SymbolTable()


def main():
    parser0=Parser()
    current_address=0
    while(1):
        if not(parser0.hasMoreCommands()):
            break

        parser0.advance()
        pre_command_type=parser0.commandType()
        if(pre_command_type==0 or pre_command_type==1):
            current_address+=1
        elif(pre_command_type==2):
            symboltable.addEntry(parser0.symbol(), current_address)

    parser0.finish()
    

    parser=Parser()
    ram_address=16
    while(1):    
        if not(parser.hasMoreCommands()):
            break
        export=""
        parser.advance()
        command_type=parser.commandType()
        if(command_type==0):
            command_symbol=parser.symbol()
            if(command_symbol.isdecimal()):
                symbol_address=int(command_symbol)
                
            else:
                if(symboltable.contains(command_symbol)):
                    symbol_address=symboltable.getAddress(command_symbol)
                    
                else:
                    symboltable.addEntry(command_symbol, ram_address)
                    symbol_address=symboltable.getAddress(command_symbol)
                    ram_address+=1

            binary=format(symbol_address, 'b')
            length=len(binary)
            for _ in range(16-length):
                export += "0"
            export += binary

        elif(command_type==1):
            command_dest=parser.dest()
            command_comp=parser.comp()
            command_jump=parser.jump()

            code_dest=code.dest(command_dest)
            code_comp=code.comp(command_comp)
            code_jump=code.jump(command_jump)

            export += "111"+code_comp+code_dest+code_jump

        elif(command_type==2):
            continue
        
        parser.write(export)

    parser.finish()
    



if __name__ == '__main__':
    main()