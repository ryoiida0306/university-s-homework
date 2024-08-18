/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 2.5 - simpleBeep
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initPWM();

//-----------------------------------------------

int main(void)
{	
	//System Initialization
	initARM();
	initPWM();
	
	//LED Configuration
	STM_EVAL_LEDInit(LED3);
	
	//Push-Button Configuration
	STM_EVAL_PBInit(BUTTON_USER,BUTTON_MODE_GPIO);
	  
	//Main Loop
	while(true) {
		//Get push-button state
		unsigned int n = STM_EVAL_PBGetState(BUTTON_USER);
		
		if(n==0) {
			STM_EVAL_LEDOff(LED3);	//disable green LED
			TIM_Cmd(TIM2, DISABLE);	//disable buzzer PWM
		}
		else {
			STM_EVAL_LEDOn(LED3);	//enable green LED
			TIM_Cmd(TIM2, ENABLE);	//enable buzzer PWM
		}
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOB, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);
	
	//GPIO Configuration (buzzer=PB.3)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	//Alternate Function Configuration
	GPIO_PinAFConfig(GPIOB, GPIO_PinSource3, GPIO_AF_2);
}

void initPWM()
{	
	uint16_t TimerPeriod = (SystemCoreClock/2000) - 1;	//2kHz
	
	//Timer Configuration
	TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;
	TIM_TimeBaseStructure.TIM_Prescaler = 0;
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;
	TIM_TimeBaseStructure.TIM_Period = TimerPeriod;
	TIM_TimeBaseStructure.TIM_ClockDivision = 0;
	TIM_TimeBaseStructure.TIM_RepetitionCounter = 0;
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseStructure);

	//PWM Configuration
	TIM_OCInitTypeDef TIM_OCInitStructure;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1;
	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable;
	TIM_OCInitStructure.TIM_OutputNState = TIM_OutputNState_Enable;
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High;
	TIM_OCInitStructure.TIM_OCNPolarity = TIM_OCNPolarity_Low;
	TIM_OCInitStructure.TIM_OCIdleState = TIM_OCIdleState_Set;
	TIM_OCInitStructure.TIM_OCNIdleState = TIM_OCIdleState_Reset;

	TIM_OCInitStructure.TIM_Pulse = (uint16_t)(((uint32_t)5*(TimerPeriod-1))/10);	//50% duty-cycle
	TIM_OC2Init(TIM2, &TIM_OCInitStructure);
}
