$ Length unit:                    millimeter (mm)
$ Time unit:                      second (s)
$ Mass unit:                      tonne (T)
$ Force unit:                     Newton (N)
$ Young�s Modulus unit:           Mpa (N/mm^2)
$ Density:                        kg/mm^3
$ Stress unit:                    Mpa (N/mm^2)
$ Acceleration due to gravity:    0 mm/s^2
$ Author:                         DaN, DaL, DaZ
$ Company:                        The Living, Autodesk
$ Date:                           02/23/2017
$ Version:                        1.0
$ Update:                         Test Lattice
$ FEM Description:                2 Pressure Load         
$ ----------------------------------------------------------------------------
$   Analysis   : Linear Static
$ ----------------------------------------------------------------------------


$test nastrynamo - dyn to nas writer

SOL 101
CEND
ECHO = NONE
TITLE = 
DISPLACEMENT(PLOT) = ALL
FORCE(PLOT,CORNER) = ALL
VOLUME 1, SET ALL, SYSTEM BASIC
SUBCASE 1
   SPC  = 1
   LOAD = 1
   STRAIN(PLOT,CORNER) = ALL
   STRESS(PLOT,CORNER) = ALL
   GPFORCE(PLOT) = ALL
   OLOAD(PLOT,REAL,RALL) = ALL
BEGIN BULK 

 
$Parameter                                                                      
PARAM,POST,-1
PARAM,OGEOM,NO
PARAM,AUTOSPC,YES
PARAM,GRDPNT,0
   
PARAM,ELEMRSLTCORD,ELEMENT
PARAM,ELEMGEOMCHECKS,OFF


                                                                                                                
GRAV    99998           9814.56 0.      16.     -1.    



$start pbar
PBAR    101     101     3.14159 0.7853970.7853971.57079                         
        0.      0.      0.      1.      1.      0.      1.      1.              
        2.7851  2.7851    


$pbar r = 0.5
PBAR    1000    101     0.78539 0.04908 0.04908 0.09817 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 0.6
PBAR    1001    101     1.13097 0.10178 0.10178 0.20357 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 0.7
PBAR    1002    101     1.53937 0.18857 0.18857 0.37714 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 0.8
PBAR    1003    101     2.01061 0.32169 0.32169 0.64339 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 0.9
PBAR    1004    101     2.54468 0.51529 0.51529 1.03059 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.0
PBAR    1005    101     3.14159 0.78539 0.78539 1.57079 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.1
PBAR    1006    101     3.80132 1.14990 1.14990 2.29980 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.2
PBAR    1007    101     4.52388 1.62860 1.62860 3.25720 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.3
PBAR    1008    101     5.30928 2.24317 2.24317 4.48634 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.4
PBAR    1009    101     6.15751 3.01718 3.01718 6.03436 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.5
PBAR    1010    101     7.06857 3.97607 3.97607 7.95214 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.6
PBAR    1011    101     8.04247 5.14718 5.14718 10.2943 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.7
PBAR    1012    101     9.07919 6.55971 6.55971 13.1194 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.8
PBAR    1013    101     10.1787 8.24478 8.24478 16.4895 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 1.9
PBAR    1014    101     11.3411 10.2353 10.2353 20.4707 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.0
PBAR    1015    101     12.5663 12.5663 12.5663 25.1327 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.1
PBAR    1016    101     13.8544 15.2744 15.2744 30.5489 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.2
PBAR    1017    101     15.2052 18.3984 18.3984 36.7968 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.3
PBAR    1018    101     16.6190 21.9786 21.9786 43.9572 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.4
PBAR    1019    101     18.0955 26.0576 26.0576 52.1152 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.5
PBAR    1020    101     19.6349 30.6795 30.6795 61.3591 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.6
PBAR    1021    101     21.2371 35.8907 35.8907 71.7815 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.7
PBAR    1022    101     22.9021 41.7392 41.7392 83.4784 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.8
PBAR    1023    101     24.6300 48.2749 48.2749 96.5498 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 
$pbar r = 2.9
PBAR    1024    101     26.4207 55.5496 55.5496 111.099 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.

$pbar r = 3.0
PBAR    1025    101     28.2743 63.6171 63.6171 127.234 
        0.      0.      0.      0.      0.      0.      0.      0.
        0.      0.
 

$end pbar


MAT1    101     72394.          0.33    2.68-9  2.09-5                                                                                                
MAT4    101     0.113   0.      
                             
                  
PSHELL  102     101     1.      101             101  


$--- ---1-------2-------3-------4-------5-------6-------7-------8-------9-------0   
$cquad4                                        
CQUAD4  10000000102     20000001200000032000000420000002                   



$start Grid
GRID    20000001        0.0     0.0     0.0                                                   
GRID    20000002        0.0     2.0     0.0    
GRID    20000003        0.0     0.0     2.0    
GRID    20000004        0.0     2.0     2.0    
GRID    20000005        8.0     0.0     0.0 
$end Grid





CBAR    600000001005    50000002500000031.      1.      1.  
CBAR    600000011000    50000003500000041.      1.      1.  
CBAR    600000021005    50000004500000051.      1.      1.  
CBAR    600000031023    50000004500000061.      1.      1.  
CBAR    600000041000    50000006500000071.      1.      1.  
CBAR    600000051023    50000007500000031.      1.      1.  
CBAR    600000061000    50000007500000081.      1.      1.  
CBAR    600000071000    50000008500000091.      1.      1.  
CBAR    600000081000    50000009500000061.      1.      1.  
CBAR    600000091000    50000009500000101.      1.      1.  
CBAR    600000101014    50000010200000051.      1.      1.  
CBAR    600000111005    20000005500000081.      1.      1.  
CBAR    600000121014    50000009200000051.      1.      1.  
CBAR    600000131000    50000010500000081.      1.      1.  
CBAR    600000141000    50000009500000071.      1.      1.  
CBAR    600000151005    50000006500000081.      1.      1.  
CBAR    600000161005    50000006500000031.      1.      1.  
CBAR    600000171014    50000004500000071.      1.      1.  
CBAR    600000181000    50000002500000041.      1.      1.  
CBAR    600000191024    50000005500000031.      1.      1.  
CBAR    600000201024    50000011500000041.      1.      1.  
CBAR    600000211014    50000005500000121.      1.      1.  
CBAR    600000221014    50000012500000061.      1.      1.  
CBAR    600000231005    50000013500000041.      1.      1.  
CBAR    600000241005    50000013500000091.      1.      1.  
CBAR    600000251000    50000014500000061.      1.      1.  
CBAR    600000261000    50000015500000091.      1.      1.  
CBAR    600000271000    50000014500000101.      1.      1.  
CBAR    600000281000    50000015500000101.      1.      1.  
CBAR    600000291000    50000014500000151.      1.      1.  
CBAR    600000301005    50000014500000131.      1.      1.  
CBAR    600000311000    50000009500000141.      1.      1.  
CBAR    600000321000    50000013500000061.      1.      1.  
CBAR    600000331024    50000012500000131.      1.      1.  
CBAR    600000341024    50000012500000111.      1.      1.  
CBAR    600000351000    50000004500000121.      1.      1.  
CBAR    600000361024    20000003500000161.      1.      1.  
CBAR    600000371000    50000017500000181.      1.      1.  
CBAR    600000381024    50000018200000031.      1.      1.  
CBAR    600000391024    50000018500000191.      1.      1.  
CBAR    600000401000    50000019500000201.      1.      1.  
CBAR    600000411000    50000021500000221.      1.      1.  
CBAR    600000421024    50000022500000191.      1.      1.  
CBAR    600000431024    50000022500000111.      1.      1.  
CBAR    600000441000    50000011500000051.      1.      1.  
CBAR    600000451024    50000022500000051.      1.      1.  
CBAR    600000461023    50000011500000211.      1.      1.  
CBAR    600000471024    50000022500000201.      1.      1.  
CBAR    600000481024    50000019500000211.      1.      1.  
CBAR    600000491024    50000019500000171.      1.      1.  
CBAR    600000501024    50000018500000201.      1.      1.  
CBAR    600000511023    50000016500000181.      1.      1.  
CBAR    600000521024    20000003500000171.      1.      1.  
CBAR    600000531023    50000016500000231.      1.      1.  
CBAR    600000541023    20000001500000171.      1.      1.  
CBAR    600000551024    50000017500000241.      1.      1.  
CBAR    600000561024    50000020500000231.      1.      1.  
CBAR    600000571024    50000020500000251.      1.      1.  
CBAR    600000581024    50000021500000241.      1.      1.  
CBAR    600000591024    50000005500000251.      1.      1.  
CBAR    600000601024    50000021500000021.      1.      1.  
CBAR    600000611024    50000002500000251.      1.      1.  
CBAR    600000621000    50000005500000021.      1.      1.  
CBAR    600000631024    50000021500000051.      1.      1.  
CBAR    600000641014    50000021500000201.      1.      1.  
CBAR    600000651000    50000025500000211.      1.      1.  
CBAR    600000661023    50000024500000251.      1.      1.  
CBAR    600000671024    50000024500000231.      1.      1.  
CBAR    600000681000    50000020500000241.      1.      1.  
CBAR    600000691024    50000017500000201.      1.      1.  
CBAR    600000701005    50000017500000161.      1.      1.  
CBAR    600000711000    50000023500000171.      1.      1.  
CBAR    600000721024    20000001500000231.      1.      1.  
CBAR    600000731024    50000016200000011.      1.      1.  

$pbar_txt

GRID    50000002        4.0     0.0     0.0       
GRID    50000003        5.0     0.0     0.0       
GRID    50000004        5.0     0.0     1.0       
GRID    50000005        4.0     0.0     1.0       
GRID    50000006        6.0     0.0     1.0       
GRID    50000007        6.0     0.0     0.0       
GRID    50000008        7.0     0.0     0.0       
GRID    50000009        7.0     0.0     1.0       
GRID    50000010        8.0     0.0     1.0       
GRID    50000011        4.0     0.0     2.0       
GRID    50000012        5.0     0.0     2.0       
GRID    50000013        6.0     0.0     2.0       
GRID    50000014        7.0     0.0     2.0       
GRID    50000015        8.0     0.0     2.0       
GRID    50000016        0.0     0.0     1.0       
GRID    50000017        1.0     0.0     1.0       
GRID    50000018        1.0     0.0     2.0       
GRID    50000019        2.0     0.0     2.0       
GRID    50000020        2.0     0.0     1.0       
GRID    50000021        3.0     0.0     1.0       
GRID    50000022        3.0     0.0     2.0       
GRID    50000023        1.0     0.0     0.0       
GRID    50000024        2.0     0.0     0.0       
GRID    50000025        3.0     0.0     0.0       
$end Grid



$cbar
                        

FORCE   1       20000005        999.    0.0     0.0     1.0
                                                                                                                
LOAD    1       1.      1.      10000   1.      10001   1.      99999           
        1.      99998   0.      99994   0.      99993        


SPC     1       20000001123456
SPC     1       20000002123456
SPC     1       20000003123456
SPC     1       20000004123456


                                                   
ENDDATA


                                               










































































