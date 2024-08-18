package dbtest;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBTest {
	public static void main(String args[]) {
		try {
			Class.forName("org.sqlite.JDBC");
			Connection con = null;
			con = DriverManager.getConnection("jdbc:sqlite:C://Users//iida ryo//Desktop//名工大授業//三年生前期//プログラミング応用//testdb.db");
			PreparedStatement pstmt = con.prepareStatement("select * from account where id=?");
			pstmt.setInt(1, 1);
			ResultSet rs = pstmt.executeQuery();
			while(rs.next()) {
				System.out.println(rs.getString("name") + ":" + rs.getInt("amount"));
			}
			rs.close();
			pstmt.close();
			con.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}

}
