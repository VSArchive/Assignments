jmp start
start: nop

LDA 8c00H
MOV H, A
LDA 8c01H
SUB H
STA 8c02H

hlt