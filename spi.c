#include<stdio.h>
#include<wiringPi.h>

#define mosi 0
#define miso 1
#define cs   2
#define scl  3

void __init__()
{
wiringPiSetup();
pinMode(0,OUTPUT);
pinMode(1,INPUT);
pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
}

int adc_read()
{
 digitalWrite(cs,0);
 /*start bit*/
 digitalWrite(scl,0);
 digitalWrite(mosi,1);
 digitalWrite(scl,1);
 /*single ended*/
 digitalWrite(scl,0);
 digitalWrite(mosi,1);
 digitalWrite(scl,1);
 /* d2 */
 digitalWrite(scl,0);
 digitalWrite(mosi,1);
 digitalWrite(scl,1);
 /* d1 */
 digitalWrite(scl,0);
 digitalWrite(mosi,0);
 digitalWrite(scl,1);

 /* d0 */
 digitalWrite(scl,0);
 digitalWrite(mosi,0);
 digitalWrite(scl,1);

 /* T sample bit dont´t care*/
 digitalWrite(scl,0);
 digitalWrite(mosi,1);
 digitalWrite(scl,1);

 /* null bit*/
 digitalWrite(scl,0);
 digitalWrite(mosi,1);
 digitalWrite(scl,1);

 int data=0,i;
 
 for(i=11;i>=0;i--)
 {
 digitalWrite(scl,0);
 if(digitalRead(miso)==1)
     data |=(1<<i);
 digitalWrite(scl,1);
 }
 printf("%d\n",data);
 digitalWrite(cs,1);
 return data;
}

main()
{
 
int data;
 __init__();
while(1)
{
system("clear");
data=adc_read();
printf("%d\n",data);
sleep(1);
}
}
