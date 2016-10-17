import java.io.*;
import java.nio.channels.*;
import java.util.Scanner;
import java.nio.ByteBuffer;

public class SharedMemory
{
	static String num1="";
	static String num2="";
	static ByteBuffer buff;
	static 	String str=null;
	public static void main(String args[]) throws IOException, InterruptedException 
	{
		Scanner scan = new Scanner(System.in);
		num1=scan.next();
		num2=scan.next();
		File file =new File("input.txt");
		BufferedWriter writer = new BufferedWriter(new FileWriter(file));
		writer.write(num1);
		writer.write("\n");
		writer.write(num2);
		writer.close();
		
				
		FileChannel channel = new RandomAccessFile(file,"rw").getChannel();
		buff = channel.map(FileChannel.MapMode.READ_ONLY,0,(int) channel.size());
		
		Thread t1=new Thread()
		{
			public void run()
			{
				 str=getString();
				 num1=str.split("\n")[0];
				 long threadId = Thread.currentThread().getId();
				 System.out.println("Thread id " + threadId + "  read input " + num1 + "\n");
			} 
		};
		Thread t2=new Thread()
		{
			public void run()
			{
				 str=getString();
				 num2=str.split("\n")[1];
				 long threadId = Thread.currentThread().getId();
				 System.out.println("Thread id " + threadId + "  read input " + num2  +"\n");				 
			}
		};
		t1.start();
		t1.join();
		t2.start();
		t2.join();
		
		long res=multiplication(num1,num2);
		System.out.println("Result :" + res);
						
	
	}
	
	public static  String getString()
	{
		buff.position(0);
		String ans="";
		char c;
		while(buff.hasRemaining())
		{
			c=(char)buff.get();
			ans+=c;
			
		}
		
		return ans;

	}


	public static byte[] stringtoByte(String str)
	{
		int n=str.length();
		byte temp[]=new byte[n];
		for(int i=0;i<n;i++)	
		   temp[n-i-1]=(byte)(str.charAt(i)-'0');
		
		return temp;
		
	}
	public static Long  multiplication(String num1,String num2)
	{
		byte [] res = new byte[num1.length()+num2.length()];
		byte[]left=stringtoByte(num1);
		byte[]right=stringtoByte(num2);
		int rightlen=right.length;
		int leftlen = left.length;	
		byte digit;
		byte temp;
		
		for(int i=0;i<rightlen;i++)
		{
			digit= right[i];
			temp=0;
			for(int j=0;j<leftlen;j++)
			{
				temp+=res[i+j];
				temp+=digit*left[j];
				res[i+j]=(byte)(temp%10);
				temp/=10;
			}
				
			int destpos = i + leftlen;
			while(temp!=0)
			{
				temp+=res[destpos];
				res[destpos]=(byte)(temp%10);
				temp/=10;
				destpos++;
			}
		}
		
		
		//reverse and print
		
		int n=res.length;
		StringBuilder stringbuilder = new StringBuilder(n);
	
		for(int i=n-1;i>=0;i--)
			stringbuilder.append((char)(res[i]+'0'));
	
		String str= stringbuilder.toString();
		return Long.parseLong(str);
		
	}
			
}
