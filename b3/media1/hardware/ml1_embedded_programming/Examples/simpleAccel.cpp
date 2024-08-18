/*
Copyright (C) 2018, Mauricio Kugler
Nagoya Institute of Technology
Media Laboratory 1 - Embedded Programming
Example 3.2 - simpleAccel - LIS3DSH
*/

#include "stm32f0xx.h"
#include "stm32f0_discovery.h"

//Initialization Functions
void initARM();
void initUSART();
void initSPI();
void initMEMS();

//Accererometer Functions
void writeMEMS(unsigned char reg, unsigned char data);
unsigned char readMEMS(unsigned char reg);

//Global Variables
bool flag = false;

//-----------------------------------------------

int main(void)
{
	initARM();
	initUSART();
	initSPI();
	initMEMS();
	
	//LED Configuration
	STM_EVAL_LEDInit(LED3);
	
	while(true) {
		if(USART_GetFlagStatus(USART2, USART_FLAG_RXNE) != RESET) {
			unsigned int n = USART_ReceiveData(USART2);
			switch(n) {
				case 0: {
					flag = true;
					STM_EVAL_LEDOn(LED3);
				} break;
				case 1: {
					flag = false;
					STM_EVAL_LEDOff(LED3);
				} break;
			}
		}	
	}
}

void initARM()
{
	//Clock Configuration
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_GPIOA, ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART2, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_SPI1, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_SYSCFG, ENABLE);
	
	//External Interruption
	SYSCFG_EXTILineConfig(EXTI_PortSourceGPIOA, EXTI_PinSource9);
	
	EXTI_InitTypeDef EXTI_InitStructure;
	EXTI_InitStructure.EXTI_Line = EXTI_Line9;
	EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
	EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;  
	EXTI_InitStructure.EXTI_LineCmd = ENABLE;
	EXTI_Init(&EXTI_InitStructure);
	
	//Interruption Configuration
	NVIC_InitTypeDef NVIC_InitStructure;
	NVIC_InitStructure.NVIC_IRQChannel = EXTI4_15_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
}

void initUSART()
{
	//GPIO Configuration (USART2: CTS=PA.0, RTS=PA.1, TX=PA.2, RX=PA.3)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin =  GPIO_Pin_0 | GPIO_Pin_1 | GPIO_Pin_2 | GPIO_Pin_3;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_UP;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource0, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource1, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource2, GPIO_AF_1);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource3, GPIO_AF_1);

	//USART Configuration
	USART_InitTypeDef USART_InitStructure;
	USART_InitStructure.USART_BaudRate = 921600;
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;
	USART_InitStructure.USART_StopBits = USART_StopBits_1;
	USART_InitStructure.USART_Parity = USART_Parity_No;
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_RTS_CTS;
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
	USART_Init(USART2, &USART_InitStructure);
	USART_Cmd(USART2,ENABLE);
}

void initSPI()
{
	//GPIO Configuration (SPI1: SCK=PA.5, MISO=PA.6, MOSI=PA.7)
	GPIO_InitTypeDef GPIO_InitStructure;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_Level_3;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource5, GPIO_AF_0);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource6, GPIO_AF_0);
	GPIO_PinAFConfig(GPIOA, GPIO_PinSource7, GPIO_AF_0);
	
	//GPIO Configuration (SPI1: CS=PA.4)
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_SetBits(GPIOA, GPIO_Pin_4);
	
	//SPI Configuration
	SPI_I2S_DeInit(SPI1);
	SPI_InitTypeDef SPI_InitStructure;
	SPI_InitStructure.SPI_Direction = SPI_Direction_2Lines_FullDuplex;
	SPI_InitStructure.SPI_Mode = SPI_Mode_Master;
	SPI_InitStructure.SPI_DataSize = SPI_DataSize_16b;
	SPI_InitStructure.SPI_CPOL = SPI_CPOL_Low;
	SPI_InitStructure.SPI_CPHA = SPI_CPHA_1Edge;
	SPI_InitStructure.SPI_NSS = SPI_NSS_Soft;
	SPI_InitStructure.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_16;
	SPI_InitStructure.SPI_FirstBit = SPI_FirstBit_MSB;
	SPI_Init(SPI1, &SPI_InitStructure);
	SPI_Cmd(SPI1, ENABLE);
}

void initMEMS()
{
	//CTRL_REG3 (23h) pp.32
	writeMEMS(0x23,0xE8);	//INT1 = enable (pulsed, high)
	
	//CTRL_REG4 (20h) pp.33
	writeMEMS(0x20,0x37);	//fs = 12.5Hz
	//writeMEMS(0x20,0x47);	//fs = 25Hz
	//writeMEMS(0x20,0x57);	//fs = 50Hz
	//writeMEMS(0x20,0x67);	//fs = 100Hz

	//CTRL_REG5 (24h) pp.34
	writeMEMS(0x24,0x00);	// scale = [-2G +2G]
}

void writeMEMS(unsigned char reg, unsigned char data)
{		
	//Set CS low
	GPIO_ResetBits(GPIOA, GPIO_Pin_4);
	
	//Send register address & data
	while(SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_TXE) == RESET);
	SPI_I2S_SendData16(SPI1, (reg<<8) | data);
	
	//Read dummy value
	while(SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_RXNE) == RESET);
	SPI_I2S_ReceiveData16(SPI1);
	
	//Set CS high
	GPIO_SetBits(GPIOA, GPIO_Pin_4);
}

unsigned char readMEMS(unsigned char reg)
{		
	//Set CS low
	GPIO_ResetBits(GPIOA, GPIO_Pin_4);
	
	//Send register address
	while(SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_TXE) == RESET);
	SPI_I2S_SendData16(SPI1, (reg|0x80) << 8);
	
	//Receive register value
	while(SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_RXNE) == RESET);
	unsigned char data = SPI_I2S_ReceiveData16(SPI1) & 0xff;
	
	//Set CS high
	GPIO_SetBits(GPIOA, GPIO_Pin_4);
	
	return(data);
}

#ifdef __cplusplus
extern "C" {
#endif
void EXTI4_15_IRQHandler()
{
	if(EXTI_GetITStatus(EXTI_Line9) != RESET) {
		unsigned char x1 = readMEMS(0x28);	//OUT_X_L (28h) pp.39
		unsigned char x2 = readMEMS(0x29);	//OUT_X_L (29h) pp.39
		unsigned char y1 = readMEMS(0x2A);	//OUT_Y_L (2Ah) pp.39
		unsigned char y2 = readMEMS(0x2B);	//OUT_Y_L (2Bh) pp.39
		unsigned char z1 = readMEMS(0x2C);	//OUT_Z_L (2Ch) pp.39
		unsigned char z2 = readMEMS(0x2D);	//OUT_Z_L (2Dh) pp.39

		if(flag==true) {
			USART_SendData(USART2,x1);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
			
			USART_SendData(USART2,x2);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
			
			USART_SendData(USART2,y1);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
			
			USART_SendData(USART2,y2);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
			
			USART_SendData(USART2,z1);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
			
			USART_SendData(USART2,z2);
			while(USART_GetFlagStatus(USART2, USART_FLAG_TC) == RESET);
		}

		EXTI_ClearITPendingBit(EXTI_Line9);
	}
}
#ifdef __cplusplus
}
#endif





