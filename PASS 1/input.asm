START 100 - -

- MOVER AREG, ='5'
- ADD BREG, ='1'
LOOP SUB CREG, A
- MOVER AREG, ='2'
- ADD BREG, B
- MOVEM AREG, C
- SUB DREG, ='3'
NEXT ADD AREG, D
- MOVER BREG, ='4'
- ADD CREG, ='6'

A DS 1 -
B DS 2 -
C DC 5 -
D DC 7 -

- STOP - -
END - - -