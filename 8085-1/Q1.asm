jmp start
start: nop

LDA 8c00H
CMA
STA 8c01H

hlt