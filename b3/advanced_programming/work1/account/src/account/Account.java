package account;


public class Account {

	int balance;//残高
	int transferFee;//振込手数料
	String name;//預金者名

	Account(int balance,int transferFee, String name){
		this.balance = balance;
		this.transferFee = transferFee;
		this.name = name;

	}

	//target:対象者、amount:金額
	boolean transfer(Account target, int amount) {
		if(balance-amount-transferFee<0) {return false;}
		balance -= (amount+transferFee);
		target.balance += amount;
		return true;
	}

	void setTransferFee(int amount) {
		transferFee = amount;
	}
	void deposit(int amount) {
		balance += amount;

	}
	boolean withdraw(int amount) {
		if(balance<amount) {return false;}
		balance -= amount;
		return true;
	}

}
