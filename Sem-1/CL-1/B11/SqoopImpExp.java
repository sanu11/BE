import java.util.Scanner;
import com.cloudera.sqoop.*;
import com.cloudera.sqoop.tool.*;

public class SqoopImpExp {
	private static SqoopOptions options;
	private static String DBURL = "jdbc:mysql://localhost:3306/";
	private static final String USERNAME = "root";
	private static final String PASSWORD = "123";
	private static final String IMPORT_DIR = "/home/yogita/sqoop/output/";
	//used in case of import
	private static final String EXPORT_FILE = "/home/yogita/sqoop/input/data";
	//used in case of export
	private static final int MAX = 100;
	
	public static void initialize(String db, String table){
		DBURL += db;
		options = new SqoopOptions(DBURL,table);
		options.setUsername(USERNAME);
		options.setPassword(PASSWORD);
		options.setFieldsTerminatedBy(',');
		options.setLinesTerminatedBy('\n');
	}
	
	// IMPORTING.. i.e mysql table to hdfs file
	public static void mysqlToHdsf(){
		System.out.println("--------------------- IMPORT OPERATION ---------------------");
		options.setTargetDir(IMPORT_DIR);
		@SuppressWarnings("deprecation")
		ImportTool it = new ImportTool();
		int retVal = it.run(options);
		if(retVal == 0){
			System.out.println("SUCCESSFULLY Imported...");
		}
		else{
			System.out.println("ERROR");
		}
	}
	
	// EXPORTING... i.e hdfs file to mysql table
	public static void hdfsToMysql(){
		/*Scanner s = new Scanner(System.in);
		String temp=null;
		String []buffer = new String[MAX];
		System.out.println("--------------------- EXPORT OPERATION ---------------------");
		System.out.println("\nEnter column names sequencially (enter quit once done...) : ");
		System.out.println("----------------------------------------------------------- ");int i;
		for(i=0; i<MAX; ++i){
		System.out.print("Enter column name ("+i+") : ");
		temp = s.next();
		if(temp.equalsIgnoreCase("quit"))
		break;
		buffer[i] = temp.toString();
		}
		String []columns = new String[i];
		for(int j=0; j<i; ++j)
		columns[j] = buffer[j].toString();*/
		String []columns = {"book_id", "book_title", "book_author"};
		options.setExportDir(EXPORT_FILE);
		options.setDbOutputColumns(columns);
		options.setUpdateMode(SqoopOptions.UpdateMode.AllowInsert);
		ExportTool it = new ExportTool();
		int retVal = it.run(options);
		if(retVal == 0){
			System.out.println("SUCCESSFULLY Exported...");
		}
		else{
			System.out.println("ERROR");
		}
	}
	public static void main(String []args){
		String db, table;
		int choice;
		Scanner s = new Scanner(System.in);
		do{
			System.out.print("\nEnter name of the database : ");
			db = s.next();
			System.out.print("\nEnter name of the table : ");
			table = s.next();
			initialize(db, table);
			System.out.println("====== SQOOP =====");
			System.out.println("1. MySQL to HDFS [IMPORT]");
			System.out.println("2. HDFS to MySQL [EXPORT]");
			System.out.println("3. Exit");
			System.out.print("\nEnter choice : ");
			choice = s.nextInt();
			switch(choice){
				case 1 : mysqlToHdsf(); 
					break;
				case 2 : hdfsToMysql(); 
					break;
				case 3 : System.exit(0);
					break;
				default: System.out.println("Invalid choice... Please try again...");
			}
		}while(choice != 3); 
	} 
}
