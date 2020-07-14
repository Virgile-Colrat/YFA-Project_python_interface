#-------------------------------------------------------------------
#Created by Virgile Colrat - LNIS 05/20/2020 
#
#This python module gathers the function usefull for the control of the 
#Keithley 236 instument using a KUSB-488A GPIB adapter. To function properly,
#it is needed to install the following python packages: 
#   -   pyvisa (Detailed instruction on how to install pyvisa
#       on MAC, Windows or linux https://pyvisa.readthedocs.io/en/1.8/getting.html)
#   -   time
#A detailed list of all the commands available to the Keithley 236
#instrument can be found here:
#https://www.tek.com/manual/model-236-237-238-source-measure-units-operators-manual-rev-e-13-mb
#There is 2 types of function in this module, the basic function (found in instrument
# documentation) and "advance" function that are a combination of basic function and are used
#to simplify the use of the instrument in this experiment
#-------------------------------------------------------------------

import pyvisa
import time

#error: disply error message in terminal for debugging purposes
def error(functionError):
    print("Command error in function \"", functionError,"\", command not recognized")

#########################################################
##                 basic functions                     ##
##  The following functions are the direct application ##
##  of the functions described in the Keithley-236     ##
##  documentation                                      ##
#########################################################    

# ModifySweepList: Modify sweep list points
def ModifySweepList(instr, level, range, delay, first, last):#A(level),(range),(delay),first(,last)
    instr.write("A"+ str(level)+','+ str(range)+','+ str(delay)+','+ str(first)+','+ str(last)+'X')

#BiasOperation: Select bias operation
def BiasOperation(instr,level, range, delay):#B(level),(range),(delay)
    instr.write("B"+ str(level)+","+ str(range)+","+str(delay)+'X')

#Calibration: Calibrate instrument
def Calibration(instr,step, value):#C step (,value) X
    instr.write("C"+ str(step)+','+str(value)+'X')

#Display:   D0: Return display to normal
#           D1,aaa ... aX: Display ASCII characters (18 max.) 
#           D2,aaa ... aX Display and store ASCII characters (18 max.)
def Display(instr,D,data):#DOX/D1,aaa ... aX/D2,aaa ... aX
    if D=="D0":
        instr.write("D0X")
    elif D[0]=='D' and int(D[1], 10) in range(1,3):
         instr.write(D+','+str(data)+'X')
    else:
        error("Display")

#SourceAndFunction: Select source (V or I) and function (dc or sweep)
def SourceAndFunction(instr,source, function):#F(source) ,(function)
    instr.write("F"+str(source)+','+ str(function)+'X')

#OutputDataFormat: Select items included, format, and lines per talk in output
def OutputDataFormat(instr,items, format, lines):#G(items) ,(format) ,(lines)
    instr.write("G"+str(items)+','+str(format)+','+str(lines)+'X')

#IEEEImmediateTrigger: Cause an immediate bus trigger
def IEEEImmediateTrigger(instr):#H0X
    instr.write("H0X")

#SelfTests: JOX Restore factory defaults
#           J1X Perform memory test
#           J2X Perform display test
def SelfTests(instr,J):#J0X/J1X/J2X
    if J[0]=='J' and int(J[1], 10) in range(0,3):
         instr.write(J+'X')
    else:
        error("SelfTests")

#EOIAndBusHoldOff:  K0: Enable EOI, enable hold-off on X
#                   K1: Disable EOI, enable hold-off on X
#                   K2: Enable EOI, disable hold-off on X
#                   K3: Disable EOI, disable hold-off on X
def EOIAndBusHoldOff(instr,K):#K0/K1/K2/K3
    if K[0]=='K' and int(K[1], 10) in range(0,4):
         instr.write(K+'X')
    else:
        error("EOIAndBusHoldOff")

#Compliance: Set compliance level and range
def Compliance(instr,level, range):#L(level) ,(range)
    instr.write("L"+str(level)+','+str(range)+'X')

#SRQMaskAndSerialPollByte: Select conditions that will cause a service-request
def SRQMaskAndSerialPollByte(instr,mask, compliance):#M(mask),(compliance)
    instr.write("M"+str(mask)+','+str(compliance)+'X')
#Operate:   N0: Place unit in standby mode
#           N1 Place unit in operate mode
def Operate(instr,N):#N0/N1
    if N[0]=='N' and int(N[1],10) in range(0,2):
         instr.write(N+'X')
    else:
        error("Operate")
#OutputSense:   O0 Select local sensing 3.6.13
#                O1:Select remote sensing
def OutputSense(instr,O):#O0/O1
    if O[0]=='O' and int(O[1], 10) in range(0,2):
         instr.write(O+'X')
    else:
        error("OutputSense")

#Filter:    P0: Measurement filter disabled
#           P1: 2-reading filter
#           P2: 4-reading filter
#           P3: B-reading filter
#           P4: 16-reading filter
#           P5: 32-reading filter
def Filter(instr,P):#P0/P1/P2/P3/P4/P5
    if P[0]=='P' and int(P[1], 10) in range(0,6):
         instr.write(P+'X')
    else:
        error("Filter")

#CreateAppendSweepList: QO,(level),(range),(delay),(count): Create fixed level sweep
#                       Q1 ,(start) ,(stop) ,(step),(range),(delay): Create linear stair sweep
#                       Q2,(start) ,(stop) ,(points) ,(range),(delay): Create logarithmic stair sweep
#                       Q3,(level),(range),(pulses),(toN),(toFF): Create fixed level pulsed sweep
#                       Q4,(start) ,(stop) ,(step) ,(range),(toN),(toFF): Create linear stair pulsed sweep
#                       Q5,(start),(stop),(points),(range),(toN),(toFF): Create logarithmic stair pulsed sweep
#                       Q6,(level),(range),(delay),(count): Append fixed level sweep
#                       Q7, (start),(stop),(step),(range),(delay): Append linear stair sweep
#                       Q8,(start),(stop),(points),(range),(delay): Append logarithmic stair sweep
#                       Q9,(level),(range),(pulses),(toN),(toFF): Append fixed level pulsed sweep
#                       Q10 ,(start) ,(stop) ,(step) ,(range),(toN),(toFF): Append linear stair pulsed sweep
#                       Q11,(start),(stop),(points),(range),(toN),(toFF): Append logarithmic stair pulsed sweep
def CreateAppendSweepList(instr,Q, level, range, delay, count, start, stop, step, points,pulses, toN, toFF ):#Q0/Q1/Q2/Q3/Q4/Q5/Q6/Q7/Q8/Q9/Q10/Q11
    if Q=="Q0":
        instr.write("Q0"+str(level)+','+str(range)+','+str(delay)+','+ str(count)+'X')
    elif Q=="Q1":
        instr.write("Q1"+str(start)+','+str(stop)+','+str(step)+','+str(range)+','+str(delay)+'X')
    elif Q=="Q2":
        instr.write("Q2"+str(start)+','+str(stop)+','+str(points)+','+str(range)+','+str(delay)+'X')
    elif Q=="Q3":
        instr.write("Q3"+str(level)+','+str(range)+','+str(pulses)+','+str(toN)+','+str(toFF)+'X')
    elif Q=="Q4":
        instr.write("Q4"+str(start)+','+str(stop)+','+str(step)+','+str(range)+','+str(toN)+','+str(toFF)+'X')
    elif Q=="Q5":
        instr.write("Q5"+ str(start)+','+str(stop)+','+str(points)+','+str(range)+','+str(toN)+','+str(toFF)+'X')
    elif Q=="Q6":
        instr.write("Q6"+ str(level)+','+str(range)+','+str(delay)+','+str(count)+'X')
    elif Q=="Q7":
        instr.write("Q7"+ str(start)+','+str(stop)+','+str(step)+','+str(range)+','+str(delay)+'X')
    elif Q=="Q8":
        instr.write("Q8"+ str(start)+','+str(stop)+','+str(points)+','+str(range)+','+str(delay)+'X')
    elif Q=="Q9":
        instr.write("Q9"+ str(level)+','+str(range)+','+str(pulses)+','+str(toN)+','+str(toFF)+'X')
    elif Q=="Q10":
        instr.write("Q10"+ str(start)+','+str(stop)+','+str(step)+','+str(range)+','+ str(toN)+','+str(toFF)+'X')
    elif Q=="Q11":
        instr.write("Q11"+ str(start)+','+str(stop)+','+str(points)+','+str(range)+','+str(toN)+','+ str(toFF)+'X')
    else:
        error("CreateAppendSweepList")
#TriggerControl:    RO Disable input/ output triggers
#                   R1 Enable input/ output triggers
def TriggerControl(instr,R):#R0/R1
    if R[0]=='R' and int(R[1],10) in range(0,2):
         instr.write(R+'X')
    else:
        error("TriggerControl")

#IntegrationTime:   S0 416 usec integration time 3.6.17
#                   S1 4 msec integration time
#                   S2 16.67 msec integration time
#                   S3 20 msec integration time
def IntegrationTime(instr,S):#S0/S1/S2/S3
    if S[0]=='S' and int(S[1], 10) in range(0,4):
         instr.write(S+'X')
    else:
        error("IntegrationTime")

#TriggerConfiguration:  Program trigger origin, effect, output trigger time, and sweep end trigger
def TriggerConfiguration(instr,origin, In, out, end):#T( origin) ,(in),( out),( end)
    instr.write("T"+str(origin)+','+str(In)+','+str(out)+','+str(end)+'X')
#Status:U0 Send model no. and revision 3.6.19
#       U1 Send error status word
#       U2 Send stored ASCII string
#       U3 Send machine status word
#       U4 Send measurement parameters us Send compliance value
#       U6 Send suppression value
#       U7 Send calibration status word
#       U8 Send defined sweep size
#       U9 Send warning status word
#       U10 Send first sweep point in compliance
#       Ull Send sweep measure size
def Status(instr, U):#U0/U1/U2/U3/U4/U5/U6/U7/U8/U9/U10/U11
    if U[0]=='U' and int(U[1], 10) in range(0,12):
         instr.write(U+'X')
    else:
        error("Status")
#DefaultDelay:  W0 Disable default delay
#               W1 Enable default delay
def DefaultDelay(instr,W):#W0/W1
    if W[0]=='W' and int(W[1], 10) in range(0,2):
         instr.write(W+'X')
    else:
        error("DefaultDelay")
#########################################################
##               Advanced functions                    ##
#########################################################   

def SetVoltage(instr, voltage):
    SourceAndFunction(instr, 0,0)
    IEEEImmediateTrigger(instr) 
    OutputDataFormat(instr,5, 2, 0)
    BiasOperation(instr,voltage, 0, 0)


def SetCurrent(instr, current):
    SourceAndFunction(instr, 0,0)
    IEEEImmediateTrigger(instr) 
    OutputDataFormat(instr,5, 2, 0)
    BiasOperation(instr,current, 1, 0)

#def SetVoltageDegra(instr, voltage):
#    instr.write("F0,0X")                                 # Force Force V measure I
#    instr.write("H0X")                                   # Immediate trigger
#    instr.write("G5,2,0X")                               # source and measure
#    instr.write("B" +str(voltage) +",0,0X")

def MeasureAndPrint(instr, timeStep, nbMeasure):
    for i in range(nbMeasure):
        Operate(instr,"N1")
        time.sleep(timeStep)                             # Wait
        print(instr.read())                     # read and print measurement from SMU
        time.sleep(timeStep)
    Operate(instr,"N0")

def MeasureAndReturn(instr, timeStep):
    Operate(instr,"N1")
    time.sleep(timeStep)                             # Wait
    return(instr.read())                     # read and return measurement from SMU