EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:LED D1
U 1 1 5F19B330
P 5800 2750
F 0 "D1" V 5839 2632 50  0000 R CNN
F 1 "LED" V 5748 2632 50  0000 R CNN
F 2 "LED_SMD:LED_Cree-XB" H 5800 2750 50  0001 C CNN
F 3 "~" H 5800 2750 50  0001 C CNN
	1    5800 2750
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R2
U 1 1 5F19BCC6
P 6350 2750
F 0 "R2" V 6154 2750 50  0000 C CNN
F 1 "56ohm" V 6245 2750 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6350 2750 50  0001 C CNN
F 3 "~" H 6350 2750 50  0001 C CNN
	1    6350 2750
	0    1    1    0   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J1
U 1 1 5F19DDA2
P 6950 2750
F 0 "J1" H 7030 2792 50  0000 L CNN
F 1 "Conn_01x03" H 7030 2701 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 6950 2750 50  0001 C CNN
F 3 "~" H 6950 2750 50  0001 C CNN
	1    6950 2750
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:2N7002 Q1
U 1 1 5F19E77C
P 5250 3200
F 0 "Q1" H 5454 3246 50  0000 L CNN
F 1 "2N7002" H 5454 3155 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 5450 3125 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7002.pdf" H 5250 3200 50  0001 L CNN
	1    5250 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 2350 6750 2650
Wire Wire Line
	6450 2750 6750 2750
Wire Wire Line
	6600 3500 6600 2850
Wire Wire Line
	6600 2850 6750 2850
$Comp
L Device:R_Small R1
U 1 1 5F1AE21E
P 6250 2350
F 0 "R1" V 6054 2350 50  0000 C CNN
F 1 "56ohm" V 6145 2350 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6250 2350 50  0001 C CNN
F 3 "~" H 6250 2350 50  0001 C CNN
	1    6250 2350
	0    1    1    0   
$EndComp
Wire Wire Line
	6750 2350 6350 2350
Wire Wire Line
	4950 2350 4950 3200
Wire Wire Line
	4950 3200 5050 3200
Wire Wire Line
	4950 2350 6150 2350
Wire Wire Line
	5350 2750 5350 3000
Wire Wire Line
	5350 2750 5650 2750
Wire Wire Line
	5350 3400 5350 3500
Wire Wire Line
	5350 3500 6600 3500
Wire Wire Line
	5950 2750 6250 2750
Text Label 6000 3500 0    50   ~ 0
GND
Text Label 6600 2750 0    50   ~ 0
5V
$EndSCHEMATC
