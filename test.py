(Established under the Presidency University Act, 2013 of the Karnataka Act 41 of 2013)
IOT LAB Programs
Name:
Id Number:
Section: 5BCA
Course code and title: CSA 3005 -Internet Of Things
ID Number: 5BCA NAME
2 | P a g e
Table Of Contents:
Experiment
No. Name of the Experiment Date
1 Blinking of an LED or using Buzzer
2 Blinking of two LED’s
3 Blinking of odd and even LED’s
4 Scrolling of LED’s
5 Controlling of LED using switch. 6 Controlling of multiple LED’s using single
switch. 6A Controlling of multiple LED’s using multiple
switches. 7 Implementation of traffic control system
8 Fading of an LED using Potentiometer. 8A Fading of an LED without using
Potentiometer
9 Controlling of servo motor using
potentiometer
9A Controlling of servo motor without using
potentiometer. 10 Implementation of IR and PIR sensor using
Arduino
ID Number: 5BCA NAME
3 | P a g e
Experiment no:1 DATE:
Aim of the experiment: To blink an LED on Arduino Uno and to verify the
result on Arduino IDE. Components required: To blink an LED on Arduino Uno the following
components are required.  Arduino Uno R3
 1 Led
 1k Ω Resistor
 Small Breadboard
 Jumper Wires
Initial circuit design:
Arduino sketch:
void setup()
{
pinMode(13, OUTPUT);
Serial.begin(9600);
ID Number: 5BCA NAME
4 | P a g e
}
void loop()
{
digitalWrite(13, HIGH);
Serial.println("Led is On");
delay(1000); // Wait for 1000 millisecond(s)
digitalWrite(13, LOW);
Serial.println("Led is Off");
delay(1000); // Wait for 1000 millisecond(s)
}
Output Screenshot:
Outcome: Led was blinked successfully for every one second
ID Number: 5BCA NAME
5 | P a g e
1(i) DATE:
Additional programs:
Aim of the experiment: To blink two LED’s on Arduino Uno and to verify the
result on Arduino IDE. Components required: To blink an LED on Arduino Uno the following
components are required.  Arduino Uno R3
 2 Led
 2 1k Ω Resistor
 Small Breadboard
 Jumper Wires
Initial circuit design:
Arduino sketch:
int led1=13;
int led2=12;
void setup()
{
pinMode(13, OUTPUT);
ID Number: 5BCA NAME
6 | P a g e
Serial.begin(9600);
}
void loop()
{
digitalWrite(led1, HIGH);
Serial.println("LED1 is On");
delay(1000); // Wait for 1000 millisecond(s)
digitalWrite(led2, LOW);
Serial.println("LED2 is Off");
digitalWrite(led2, HIGH);
Serial.println("LED2 is On");
delay(1000);
digitalWrite(led1, LOW);
Serial.println("LED1 is Off");
delay(1000); // Wait for 1000 millisecond(s)
}
Output Screenshot:
ID Number: 5BCA NAME
7 | P a g e
Outcome: Two LED’s were successfully blinked alternatively for every one second.
ID Number: 5BCA NAME
8 | P a g e
1(ii) DATE:
Aim of the experiment: To blink odd and even LED’s on Arduino Uno and to
verify the result on Arduino IDE. Components required: To blink odd and even LED’s on Arduino Uno the
following components are required.  Arduino Uno R3
 8 Led
 8 1k Ω Resistor
 Small Breadboard
 Jumper Wires
Initial circuit design:
Arduino sketch:
int del=1000; // variable define the delay
void setup()
{
// make pins 2, 3, 4 and up to 8 as digital output pins
ID Number: 5BCA NAME
9 | P a g e
// for loop to initialize all pins
for(int i=2; i<=8; i++)
{
pinMode(i,OUTPUT); // declare pins as a output
}
}
void loop()
{
// for loop makes an even number of digital output pins digital high
for(int i=2; i<=8; i++)
{
if(i%2==0)
{
digitalWrite(i,HIGH); delay(del);
digitalWrite(i,LOW); delay(del);
}
}/* end of for loop */
// for loop makes an odd number of digital output pins digital high
for(int i=2; i<=8; i++)
{
if(i%2==1)
ID Number: 5BCA NAME
10 | P a g e
{
digitalWrite(i,HIGH); delay(del);
digitalWrite(i,LOW); delay(del);
}
}/* end of for loop */
}/* end of main loop */
Output Screenshot:
Outcome: Odd and even LED’s were blinked successfully for every one
second
1(iii) DATE:
Aim of the experiment: To scroll LED’s on Arduino Uno and to verify the
result on Arduino IDE.
ID Number: 5BCA NAME
11 | P a g e
Components required: To scroll LED’s on Arduino Uno the following
components are required.  Arduino Uno R3
 8 Led
 8 1k Ω Resistor
 Small Breadboard
 Jumper Wires
Initial circuit design:
Arduino sketch:
int ledPins[]={2,3,4,5,6,7,8,9};
void setup()
{
for(int i=0;i<8;i++)
{
pinMode(ledPins[i], OUTPUT);
ID Number: 5BCA NAME
12 | P a g e
}
Serial.begin(9600);
}
void loop()
{
for(int i=0;i<8;i++)
{
digitalWrite(ledPins[i],HIGH); delay(1000);
digitalWrite(ledPins[i],LOW);
}
for(int i=7;i>=0;i--)
{
digitalWrite(ledPins[i],HIGH); delay(1000);
digitalWrite(ledPins[i],LOW);
}
}
Output Screenshot:
ID Number: 5BCA NAME
13 | P a g e
Outcome: Led was scrolled successfully for every one second
ID Number: 5BCA NAME
14 | P a g e
Experiment no:2 DATE:
Aim of the experiment: Interfacing of Arduino Uno with LED and switch and
to control LED using switch. Components required:To interface an Arduino Uno with LED and switch the
following components are required.  Arduino Uno R3
 Led
 1k Ω and 10k Ω Resistor
 Small Breadboard
 Jumper Wires
 Push button
Initial circuit design:
Arduino sketch:
void setup()
{
ID Number: 5BCA NAME
15 | P a g e
pinMode(13, OUTPUT);
pinMode(12, INPUT);
Serial.begin(9600);
}
void loop()
{
if(digitalRead(12)==1)
{
digitalWrite(13, HIGH);
Serial.println("LED IS ON.....");
delay(1000); // Wait for 1000 millisecond(s)
}
digitalWrite(13, LOW);
Serial.println("LED IS OFF.....");
delay(1000); // Wait for 1000 millisecond(s)
}
ID Number: 5BCA NAME
16 | P a g e
Output Screenshot:
Outcome: Arduino Uno was successfully interfaced with LED and switch and
the LED was controlled using switch.
ID Number: 5BCA NAME
17 | P a g e
2(i) DATE:
Additional programs:
Aim of the experiment: To control multiple LED’s using single switch. Components required: To control multiple LED’s using single switch the
following components are required.  Arduino Uno R3
 Led
 1k Ω and 10k Ω Resistor
 Small Breadboard
 Jumper Wires
 Push button
Initial circuit design:
Arduino sketch:
int button_pin=4;
void setup()
ID Number: 5BCA NAME
18 | P a g e
{
pinMode(button_pin,INPUT);
pinMode(13,OUTPUT);
Serial.begin(9600);
}
void loop()
{
Serial.println("Controlling LED through push button");
int button;
button=digitalRead(button_pin);
if(button==HIGH)
{
digitalWrite(13,HIGH);
Serial.println("LED1 is ON");
digitalWrite(13,HIGH);
Serial.println("LED2 is ON");
}
else
{
digitalWrite(13,LOW);
Serial.println("LED2 is OFF");
ID Number: 5BCA NAME
19 | P a g e
digitalWrite(13,LOW);
Serial.println("LED2 is OFF");
}
}
Output Screenshot:
Outcome: Multiple LED’s were controlled successfully using single switch .
ID Number: 5BCA NAME
20 | P a g e
2(ii) DATE:
Additional program:
Aim of the experiment: To control multiple LED’s using multiple switch. Components required: To control multiple LED’s using single switch the
following components are required.  Arduino Uno R3
 Led
 1k Ω and 10k Ω Resistor
 Small Breadboard
 Jumper Wires
 Push button
Initial circuit design:
Arduino sketch:
int button_pin1=4;
ID Number: 5BCA NAME
21 | P a g e
int button_pin2=5;
void setup()
{
pinMode(13, OUTPUT);
pinMode(button_pin1,INPUT);
pinMode(button_pin2,INPUT);
pinMode(12,OUTPUT);
Serial.begin(9600);
}
void loop()
{
int button1,button2;
button1=digitalRead(button_pin1);
button2=digitalRead(button_pin2);
if (button1==HIGH)
{
digitalWrite(13, HIGH);
}
else
{
digitalWrite(13,LOW);
}
if (button2==HIGH)
ID Number: 5BCA NAME
22 | P a g e
{
digitalWrite(12,HIGH);
}
else
{
digitalWrite(12,LOW);
}
}
Output Screenshot:
Outcome: Multiple LED’s were controlled successfully using multiple switch.
ID Number: 5BCA NAME
23 | P a g e
Additional program DATE:
Aim of the experiment: Arduino program to implement traffic control system. Components required: to implement traffic control system the following
components are required.  Arduino Uno R3 board
 Power cable(1)
 Breadboard(1)
 Led (5)
 2 Red LED’s
 1 Yellow LED
 2 Green LED’s
 200 Ω Resistor (6)
 Jumper Wires
 Tactile Switch (Push button)
Initial circuit design:
ID Number: 5BCA NAME
24 | P a g e
Arduino sketch:
int carRed =12;
int carYellow =11;
int carGreen =10;
int pedRed =9;
int pedGreen =8;
int button=2;
int crossTime=5000;
unsigned long changeTime;
void setup()
{
pinMode(carRed, OUTPUT);
pinMode(carYellow, OUTPUT);
pinMode(carGreen, OUTPUT);
pinMode(pedRed, OUTPUT);
pinMode(pedGreen, OUTPUT);
pinMode(button, INPUT);
digitalWrite(carGreen, HIGH);
digitalWrite(pedRed, HIGH);
}
ID Number: 5BCA NAME
25 | P a g e
void loop()
{
int state=digitalRead(button);
if(state==HIGH &&(millis()-changeTime)>5000)
{
changeLights();
}
}
void changeLights()
{
digitalWrite(carGreen,LOW);
digitalWrite(carYellow, HIGH);
delay(2000);
digitalWrite(carYellow, LOW);
digitalWrite(carRed, HIGH);
delay(1000);
digitalWrite(pedRed, LOW);
digitalWrite(pedGreen, HIGH);
delay(crossTime);
for(int x=0;x<10;x++)
{
digitalWrite(pedGreen, HIGH);
delay(250);
ID Number: 5BCA NAME
26 | P a g e
digitalWrite(pedGreen, LOW);
delay(250);
}
digitalWrite(pedRed, HIGH);
delay(500);
digitalWrite(carYellow, HIGH);
digitalWrite(carRed, LOW);
delay(1000);
digitalWrite(carGreen,HIGH);
digitalWrite(carYellow, LOW);
changeTime=millis();
}
Output Screenshot:
ID Number: 5BCA NAME
27 | P a g e
Outcome: Traffic control system was implemented successfully using
Arduino Uno. Experiment no:3 DATE:
Aim of the experiment: To adjust the brightness (Fading) of an LED using
Potentiometer. Components required:
 Arduino Uno
 Led
 Potentiometer(knob)
 Resistor
 Tinkercad simulator
Initial circuit design:
Arduino sketch:
const int analogInput=A0;
const int analogOutput=9;
ID Number: 5BCA NAME
28 | P a g e
int sensorValue=0; //wiper-read voltage from potentiometer
int outputValue=0;//value output to the PWM(analog output)
void setup()
{
Serial.begin(9600);
}
void loop()
{
sensorValue=analogRead(analogInput);
outputValue=map(sensorValue,0,1023,0,255);
analogWrite(analogOutput,outputValue);
Serial.print("Sensor=");
Serial.print(sensorValue);
Serial.print("\t Output=");
Serial.println(outputValue);
ID Number: 5BCA NAME
29 | P a g e
}
Output Screenshot:
Outcome: The brightness of an LED was adjusted successfully using Potentiometer.
ID Number: 5BCA NAME
30 | P a g e
Additional program: DATE:
Aim of the experiment: To adjust the brightness (Fading) of an LED without
using Potentiometer. Components required:
 Arduino Uno
 Led
 Resistor  Tinkercad simulator
Initial circuit design:
Arduino sketch:
const int analogOutput=9;
int sensorValue=0;
int outputValue=0;
ID Number: 5BCA NAME
31 | P a g e
void setup()
{
Serial.begin(9600);
}
void loop()
{
for(int i=0;i<=1023;i++)
{
sensorValue=analogRead(i);
outputValue=map(sensorValue,0,1023,0,255);
//map is a function which accepts 5 arguments map(input sensor
value ,volt_value range and analog value range;
analogWrite(analogOutput,outputValue);
Serial.print("Sensor=");
Serial.print(sensorValue);
Serial.print("\t Output=");
Serial.println(outputValue);
}
for(int i=1023;i>=0;i--)
{
sensorValue=analogRead(i);
ID Number: 5BCA NAME
32 | P a g e
outputValue=map(sensorValue,0,1023,0,255);
analogWrite(analogOutput,outputValue);
Serial.print("Sensor=");
Serial.print(sensorValue);
Serial.print("\t Output=");
Serial.println(outputValue);
}
}
Output Screenshot:
Outcome: The brightness of an LED was adjusted successfully without using potentiometer
ID Number: 5BCA NAME
33 | P a g e
Experiment no:4 DATE:
Aim of the experiment: Arduino program to demonstrate control of servo
motor using potentiometer. Components required:
 Arduino Uno board
 Jumper wires
 Power cable
 Servo Motor
 Potentiometer(knob)
Initial circuit design:
Arduino sketch:
ID Number: 5BCA NAME
34 | P a g e
#include<Servo.h>
Servo myservo;// servo is class ,myservo is object, tp control
servometer
int potpin=0; //potentiometer pin
void setup()
{
myservo.attach(9);//3 5 6 9 11
}
void loop()
{
int val=analogRead(potpin);
int output=map(val,0,1023,0,180);
myservo.write(output);
delay(100);
}
Output Screenshot:
ID Number: 5BCA NAME
35 | P a g e
Outcome: Control of servo motor using potentiometer was demonstrated
successfully.
ID Number: 5BCA NAME
36 | P a g e
Additional Program DATE:
Aim of the experiment: Arduino program to demonstrate control of servo
motor without using potentiometer. Components required:
 Arduino Uno board
 Jumper wires
 Power cable
 Servo Motor
Initial circuit design:
ID Number: 5BCA NAME
37 | P a g e
Arduino sketch:
#include <Servo.h>
Servo myservo;
int pos=0;
void setup()
{
myservo.attach(9);
}
void loop()
{
for(pos=0;pos<180;pos++)
{
myservo.write(pos);
delay(5);
}
for(pos=180;pos>0;pos--)
{
myservo.write(pos);
delay(5);
}
}
Output Screenshot:
ID Number: 5BCA NAME
38 | P a g e
Outcome: Control of servo motor without using potentiometer was
demonstrated successfully. Implementation of IR and PIR sensor using Arduino and Tinkercad
ID Number: 5BCA NAME
39 | P a g e
