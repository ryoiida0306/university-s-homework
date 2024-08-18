/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 2.1 - simpleTimer
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initTimer();

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	initTimer();
	
	//LED Configuration
	STM_EVAL_LEDInit(LED3);
	STM_EVAL_LEDInit(LED4);
	
	//Enable Timer
	TIM_Cmd(TIM2, ENABLE);
	TIM_Cmd(TIM3, ENABLE);
	
	//Main Loop
	while(true) {
		
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOA, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM3, ENABLE);
	
	//Interruption Configuration
	TIM_DeInit(TIM2);
	TIM_DeInit(TIM3);

	//Timer Interruption Configuration
	NVIC_InitTypeDef NVIC_InitStructure;
	NVIC_InitStructure.NVIC_IRQChannel = TIM2_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
	
	NVIC_InitStructure.NVIC_IRQChannel = TIM3_IRQn;
	NVIC_Init(&NVIC_InitStructure);
}

void initTimer()
{
	//Timer Configuration
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;
	TIM_TimeBaseStructure.TIM_Prescaler = (uint16_t)(SystemCoreClock/1000)-1;	// 1kHz
	TIM_TimeBaseStructure.TIM_Period = 250-1;									// 4Hz
	TIM_TimeBaseStructure.TIM_ClockDivision = 0;
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
	TIM_TimeBaseInit(TIM2,&TIM_TimeBaseStructure);
	
	TIM_TimeBaseStructure.TIM_Prescaler = (uint16_t)(SystemCoreClock/1000)-1;	// 1kHz
	TIM_TimeBaseStructure.TIM_Period = 1000-1;									// 1Hz
	TIM_TimeBaseInit(TIM3,&TIM_TimeBaseStructure);

	//Enable interrupts
	TIM_ITConfig(TIM2,TIM_IT_Update,ENABLE);
	TIM_ITConfig(TIM3,TIM_IT_Update,ENABLE);
}

//-----------------------------------------------

#ifdef __cplusplus
extern "C" {
#endif
void TIM2_IRQHandler()
{
	if(TIM_GetITStatus(TIM2,TIM_IT_Update) != RESET) {
		TIM_ClearITPendingBit(TIM2,TIM_IT_Update);	//Clear TIM2 IRQ
		STM_EVAL_LEDToggle(LED3);					//Toggle Green LED
	}
}

void TIM3_IRQHandler()
{
	if(TIM_GetITStatus(TIM3,TIM_IT_Update) != RESET) {
		TIM_ClearITPendingBit(TIM3,TIM_IT_Update);	//Clear TIM3 IRQ
		STM_EVAL_LEDToggle(LED4);					//Toggle Blue LED
	}
}
#ifdef __cplusplus
}
#endif
