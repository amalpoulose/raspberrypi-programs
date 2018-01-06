#include<wiringPi.h>
#include<stdio.h>

int main()
{
 int fd;
 unsigned char hr,min,sec;
 wiringPiSetup();
 if((fd=wiringPiI2CSetup(0x68))<0)
 {
	printf("Error : Device is not available");
	return;
 }
 wiringPiI2CWriteReg8(fd,0,0x53);
 wiringPiI2CWriteReg8(fd,1,0x59);
 wiringPiI2CWriteReg8(fd,2,0x23);
 while(1)
{
 system("clear");
 hr=wiringPiI2CReadReg8(fd,2);
 min=wiringPiI2CReadReg8(fd,1);
 sec=wiringPiI2CReadReg8(fd,0);
 printf("%x : %x : %x\n",hr,min,sec);
 sleep(1);
}
return 0;
}

