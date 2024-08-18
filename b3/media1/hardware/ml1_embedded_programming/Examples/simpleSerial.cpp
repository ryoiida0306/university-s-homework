/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 3.1 - simpleSerial
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initUSART();

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	initUSART();
	
	//LED Configuration
	STM_EVAL_LEDInit(LED3);
	STM_EVAL_LEDInit(LED4);
	
	unsigned int k = 48;

	//Main Loop
	while(true) {
    	if(USART_GetFlagStatus(USART2, USART_FLAG_RXNE) != RESET) {
			unsigned int n = USART_ReceiveData(USART2);

			switch(n) {
				case '1': STM_EVAL_LEDOn(LED3); break;
				case '2': STM_EVAL_LEDOn(LED4); break;
				case '3': STM_EVAL_LEDOff(LED3); break;
				case '4': STM_EVAL_LEDOff(LED4); break;
				default: USART_SendData(USART2,'X');
			}
		}

		unsigned char s1 = GPIO_ReadInputDataBit(GPIOC,GPIO_Pin_2);	//read S1 switch
		if(s1==0) {
			USART_SendData(USART2,k);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
		  
			k++;
			if(k==58) k=65;
			if(k==91) k=97;
			if(k==123) k=48;
		}
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOA, ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOC, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART2, ENABLE);
	
	//GPIO Configuration (S1=PC.2)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOC, &GPIO_InitStructure);

}

void initUSART()
{
	//GPIO Configuration (USART2: CTS=PA.0, RTS=PA.1, TX=PA.2, RX=PA.3)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource0, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource1, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource2, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource3, GPIO_AF_1);
	GPIO_InitStructure.GPIO_Pin =  GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;
	GPIO_Init(GPIOA, &GPIO_InitStructure);

	//USART Configuration
	USART_InitTypeDef USART_InitStructure;
	USART_InitStructure.USART_BaudRate = 115200;
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;
	USART_InitStructure.USART_StopBits = USART_StopBits_1;
	USART_InitStructure.USART_Parity = USART_Parity_No;
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_RTS_CTS;
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
	USART_Init(USART2, &USART_InitStructure);
	USART_Cmd(USART2,ENABLE);
}
	