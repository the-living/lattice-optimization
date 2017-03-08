$ Length unit:                    millimeter (mm)
$ Time unit:                      second (s)
$ Mass unit:                      tonne (T)
$ Force unit:                     Newton (N)
$ Young’s Modulus unit:           Mpa (N/mm^2)
$ Density:                        kg/mm^3
$ Stress unit:                    Mpa (N/mm^2)
$ Acceleration due to gravity:    0 mm/s^2
$ Author:                         Damon Lau
$ Company:                        The Living, Autodesk
$ Date:                           02/23/2017
$ Version:                        1.0
$ Update:                         Airbus VTF 
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




$cbar


                        

FORCE   1       20000005        999.    0.0     0.0     1.0
                                                                                                                
LOAD    1       1.      1.      10000   1.      10001   1.      99999           
        1.      99998   0.      99994   0.      99993        


SPC     1       20000001123456
SPC     1       20000002123456
SPC     1       20000003123456
SPC     1       20000004123456


                                                   
ENDDATA


                                               

































































