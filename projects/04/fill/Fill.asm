// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@prev
M=0
@now
M=0
(LOOP)
    @now
    D=M
    @prev
    M=D
    @i
    M=0
    @KBD
    D=M
    @NOT0
    D;JNE
    @EQ0
    D;JEQ
    
(EQ0)
    @now
    M=0
    D=M
    @prev
    D=D-M
    @LOOP
    D;JEQ

(EQ0LOOP)        
    @i
    D=M
    @SCREEN
    A=A+D
    M=0

    @i
    M=M+1

    @8192
    D=A-D
    @LOOP
    D;JEQ

    @EQ0LOOP
    0;JMP

(NOT0)
    @now
    M=1
    D=M
    @prev
    D=D-M
    @LOOP
    D;JEQ

(NOT0LOOP)
    @i
    D=M
    @SCREEN
    A=A+D
    M=-1

    @i
    M=M+1

    @8192
    D=A-D
    @LOOP
    D;JEQ

    @NOT0LOOP
    0;JMP
