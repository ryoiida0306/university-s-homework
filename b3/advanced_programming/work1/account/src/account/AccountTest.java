package account;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class AccountTest {

	@Test
	void testAccount() {
		Account a = new Account(1000,50,"sato");
		assertEquals(a.balance,1000);
		assertEquals(a.transferFee,50);
	}

	@Test
	void testTransfer() {

		Account a = new Account(1000,50,"sato");
		Account b = new Account(10000,50,"suzuki");
		a.transfer(b,200);
		assertEquals(a.balance,550);
	}

	@Test
	void testSetTransferFee() {
		Account a = new Account(1000,50,"sato");
		a.setTransferFee(30);
		assertEquals(a.transferFee,30);
	}

	@Test
	void testDeposit() {

		Account a = new Account(1000,50,"sato");
		a.deposit(500);
		assertEquals(a.balance,1500);

	}

	@Test
	void testWithdraw() {
		Account a = new Account(1000,50,"sato");
		a.withdraw(30);
		assertEquals(a.balance,970);


	}

}
