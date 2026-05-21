START:   DECI N,d
         LDA INDEX,d
LOOP:    CPA N,d
         BREQ DONE
         DECI NUM,d
         LDA SUM,d
         ADDA NUM,d
         STA SUM,d
         LDA INDEX,d
         ADDA 1,i
         STA INDEX,d
         BR LOOP
DONE:    LDA SUM,d
         DECO SUM,d
         STOP

NUM:     .BLOCK 2
SUM:     .WORD 0
N:       .BLOCK 2
INDEX:   .WORD 0
         .END