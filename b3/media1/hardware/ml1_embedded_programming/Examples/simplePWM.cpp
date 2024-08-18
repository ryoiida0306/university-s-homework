/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 2.4 - simplePWM
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initPWM();

//Utility functions
unsigned char getSwitch();
unsigned short period(unsigned int n);

//Global Variables
uint16_t TimerPeriod;
TIM_OCInitTypeDef TIM_OCInitStructure;

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	initPWM();
	
	//Enable Timer
	TIM_Cmd(TIM3, ENABLE);

	//Main Loop
	while(true) {
		unsigned char s = getSwitch();
		unsigned int p = 0;
		
		//Set duty-cycle values
		switch(s) {
			case 4: p = 250; break;
			case 2: p = 500; break;
			case 1: p = 750; break;
			default: s = 0;
		}

		//Configurate timers
		if(s>0) {
			TIM_OCInitStructure.TIM_Pulse = period(p);
			TIM_OC4Init(TIM3, &TIM_OCInitStructure);
		}
	}
}
	
void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOC, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
	
	//GPIO Configuration (S1=PC.2, S2=PC.1, S3=PC.0)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
	
	//GPIO Configuration (extra=PC.9)
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
	
	//Alternate Function Configuration
	GPIO_PinAFConfig(GPIOC, GPIO_PinSource9, GPIO_AF_1);
}

void initPWM()
{	
	TimerPeriod = (SystemCoreClock/10000) - 1;	//10kHz
	
	//Timer Configuration
	TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	TIM_TimeBaseStructure.TIM_Prescaler = 0;
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
	TIM_TimeBaseStructure.TIM_Period = TimerPeriod;
	TIM_TimeBaseStructure.TIM_ClockDivision = 0;
	TIM_TimeBaseStructure.TIM_RepetitionCounter = 0;
	TIM_TimeBaseInit(TIM3, &TIM_TimeBaseStructure);

	//PWM Configuration
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;
	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
	TIM_OCInitStructure.TIM_OutputNState = TIM_OutputNState_Enable;
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
	TIM_OCInitStructure.TIM_OCNPolarity = TIM_OCNPolarity_Low;
	TIM_OCInitStructure.TIM_OCIdleState = TIM_OCIdleState_Set;
	TIM_OCInitStructure.TIM_OCNIdleState = TIM_OCIdleState_Reset;

	TIM_OCInitStructure.TIM_Pulse = period(250);
	TIM_OC4Init(TIM3, &TIM_OCInitStructure);
}

unsigned char getSwitch()
{
	unsigned char s1 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_2);	//read S1 switch
	unsigned char s2 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_1);	//read S2 switch
	unsigned char s3 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_0);	//read S3 switch
	
	unsigned char s = (1-s1)*4 + (1-s2)*2 + (1-s3);
	return(s);
}

unsigned short period(unsigned int n)
{
	unsigned short p = (n*(TimerPeriod-1))/1000;
	return(p);
}

