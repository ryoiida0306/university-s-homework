/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 2.3 - simpleDisplay
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initADC();

//Utility functions
void display(unsigned char n);
unsigned short readADC();

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	initADC();
	
	//Main Loop
	while(true) {
		//Read ADC value
		unsigned short n = 4095 - readADC();
		
		//Adjust scale
		unsigned int f = (n*10)/4095;
		
		//Display value
		if(f<1) display('0');
		else if(f<2) display('1');
		else if(f<3) display('2');
		else if(f<4) display('3');
		else if(f<5) display('4');
		else if(f<6) display('5');
		else if(f<7) display('6');
		else if(f<8) display('7');
		else if(f<9) display('8');
		else display('9');
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOB, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1, ENABLE);
	
	//GPIO Configuration (A=PB.8, B=PB.15, C=PB.14, D=PB.10, E=PB.9, F=PB.11, G=PB.12, P=PB.13)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_13 | GPIO_Pin_14 | GPIO_Pin_15;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
}

void initADC()
{
	//GPIO Configuration (ADC.IN8=PB.0)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AN;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOB, &GPIO_InitStructure);

	//ADC Configuration
	ADC_DeInit(ADC1);
	ADC_InitTypeDef ADC_InitStruct;
	ADC_InitStruct.ADC_Resolution = ADC_Resolution_12b;
	ADC_InitStruct.ADC_ContinuousConvMode = DISABLE;
	ADC_InitStruct.ADC_ExternalTrigConvEdge = ADC_ExternalTrigConvEdge_None;
	ADC_InitStruct.ADC_ExternalTrigConv = ADC_ExternalTrigConv_T3_TRGO;
	ADC_InitStruct.ADC_DataAlign = ADC_DataAlign_Right;
	ADC_InitStruct.ADC_ScanDirection = ADC_ScanDirection_Upward;
	ADC_Init(ADC1,&ADC_InitStruct);

	ADC_ChannelConfig(ADC1, ADC_Channel_8, ADC_SampleTime_239_5Cycles);
	ADC_GetCalibrationFactor(ADC1);

	ADC_Cmd(ADC1,ENABLE);
}

void display(unsigned char n)
{
	//Clear display
	GPIO_ResetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_13 | GPIO_Pin_14 | GPIO_Pin_15);
	
	switch(n) {
		case '0': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case '1': GPIO_SetBits(GPIOB, GPIO_Pin_14 | GPIO_Pin_15); break;
		case '2': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_12 | GPIO_Pin_15); break;	
		case '3': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_10 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case '4': GPIO_SetBits(GPIOB, GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case '5': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14); break;
		case '6': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14); break;
		case '7': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case '8': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case '9': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case 'A': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case 'B': GPIO_SetBits(GPIOB, GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_14); break;
		case 'C': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11); break;
		case 'D': GPIO_SetBits(GPIOB, GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_12 | GPIO_Pin_14 | GPIO_Pin_15); break;
		case 'E': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12); break;
		case 'F': GPIO_SetBits(GPIOB, GPIO_Pin_8 | GPIO_Pin_9 | GPIO_Pin_11 | GPIO_Pin_12); break;
		case '-': GPIO_SetBits(GPIOB, GPIO_Pin_12); break;
		case '.': GPIO_SetBits(GPIOB, GPIO_Pin_13); break;
	}
}

unsigned short readADC()
{
	ADC_StartOfConversion(ADC1);

	while(ADC_GetFlagStatus(ADC1,ADC_FLAG_EOC)==RESET);
	unsigned short n = ADC_GetConversionValue(ADC1);
	
	return(n);
}
