/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 1.1 - simpleLight
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

int main(void)
{	
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOA, ENABLE);
	
	//LED Configuration
	STM_EVAL_LEDInit(LED3);
	
	//Push-Button Configuration
	STM_EVAL_PBInit(BUTTON_USER,BUTTON_MODE_GPIO);
  
	//Main Loop
	while(true) {
		//Get push-button state
		unsigned int n = STM_EVAL_PBGetState(BUTTON_USER);
		
		if(n==0) STM_EVAL_LEDOff(LED3);	//disable green LED
		else STM_EVAL_LEDOn(LED3);		//enable green LED
	}
}
