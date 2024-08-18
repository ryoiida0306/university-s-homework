/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 2.1 - simpleSwitch
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	
	//Main Loop
	while(true) {
		unsigned int s1 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_1);	//read S1 switch
		if(s1==0) GPIO_SetBits(GPIOC,GPIO_Pin_6);					//enable RGB.Red
		else GPIO_ResetBits(GPIOC,GPIO_Pin_6);						//disable RGB.Red
		
		unsigned int s2 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_2);	//read S2 switch
		if(s2==0) GPIO_SetBits(GPIOC,GPIO_Pin_7);					//enable RGB.Green
		else GPIO_ResetBits(GPIOC,GPIO_Pin_7);						//disable RGB.Green
		
		unsigned int s3 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_0);	//read S3 switch
		if(s3==0) GPIO_SetBits(GPIOC,GPIO_Pin_8);					//enable RGB.Blue
		else GPIO_ResetBits(GPIOC,GPIO_Pin_8);						//disable RGB.Blue
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOC, ENABLE);
	
	//GPIO Configuration (RGB.Red=PC.6, RGB.Green=PC.7, RGB.Blue=PC.8)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6 | GPIO_Pin_7 | GPIO_Pin_8;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
}

