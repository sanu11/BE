package com.example.sanika.calci;

import android.content.Context;
import android.renderscript.Double2;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.text.DecimalFormat;

public class MainActivity extends AppCompatActivity {
    String expr="";
    int operator = 0;
    int flag=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String filename = "input.txt";
        String expr= "3+5";
        FileOutputStream outputstream;
        try {
        outputstream = openFileOutput(filename, Context.MODE_PRIVATE);

            outputstream.write(expr.getBytes());
            outputstream.close();
            readFromFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public  void readFromFile() {

        InputStream inputstream = null;
        try {
            inputstream = getApplicationContext().openFileInput("input.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        InputStreamReader inputstreamreader = new InputStreamReader(inputstream);
        BufferedReader bufferedreader = new BufferedReader(inputstreamreader);

        StringBuilder text = new StringBuilder();
        String recvstring="";

        try {
            while((recvstring = bufferedreader.readLine())!=null){
                text.append(recvstring);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            inputstream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        double res= calculate(text.toString(),1,0);
        Log.i("My_tag", "Value read from file is : " + text.toString() + "\nResult :" + res);
    }

    public void onClickButton(View v){
        int id = v.getId();
        String temp="";
        int operate= operator;
        TextView textview = (TextView)findViewById(R.id.input);
        switch (id)
        {
            case R.id.one:
                temp = "1";
                break;
            case R.id.two:
                temp = "2";
                break;
            case R.id.three:
                temp = "3";
                break;
            case R.id.four:
                temp = "4";
                break;
            case R.id.five:
                temp = "5";
                break;
            case R.id.six:
                temp = "6";
                break;
            case R.id.seven:
                temp = "7";
                break;
            case R.id.eight:
                temp = "8";
                break;
            case R.id.nine:
                temp = "9";
                break;
            case R.id.dec:
                temp+=".";
                break;
            case R.id.zero:
                temp = "0";
                break;
            case R.id.add:
                temp+="+";
                operator=1;
                break;
            case R.id.subtract:
                temp+="-";
                operator=2;
                break;
            case R.id.multiply:
                temp+="*";
                operator=3;
                break;
            case R.id.divide:
                temp+="/";
                operator=4;
                break;

            case R.id.leftpar:
                temp+="(";
                break;
            case R.id.rightpar:
                temp+=")";
                break;
            case R.id.sin:
                flag=1;
                temp+="sin(";
                break;
            case R.id.cos:
                flag=1;
                temp+="cos(";
                break;
            case R.id.tan:
                flag=1;
                temp+="tan(";
                break;
        }
        expr +=temp;
        operate=operator;
      textview.setText(expr);

    }
    public  void onClickEqual(View v){
        double res = calculate(expr,operator,flag);
        TextView textview  = (TextView)findViewById(R.id.input);
        textview.setText(""+res);
        expr = String.valueOf(res);
        operator=0;
        flag=0;
    }

    public  void onClickDel(View v) {

        TextView textview = (TextView) findViewById(R.id.input);
        String input = textview.getText().toString();
        if (input.length() != 0){
            String newinput = input.substring(0, input.length() - 1);
            textview.setText(newinput);
            expr = newinput;
    }
}

    public void onClickClear(View v){
        TextView textview = (TextView)findViewById(R.id.input);
        textview.setText("");
        expr="";
    }
    public static double  roundThreeDecimals(double d)
    {
        DecimalFormat twoDForm = new DecimalFormat("#.###");
        return Double.valueOf(twoDForm.format(d));
    }


    public static double calculate(String expr,int operator,int flag) {
        double res=0;
        if(operator==1){
            String arr[] = expr.split("\\+");
//            Log.i("My_tag","in add "+ arr[0]);
            double num1 = Double.parseDouble(arr[0]);
            double num2 = Double.parseDouble(arr[1]);
            res= num1+num2;

        }
        else if(operator==2){
            String arr[] = expr.split("-");
//            Log.i("My_tag",""+ arr[0]);
            double num1 = Double.parseDouble(arr[0]);
            double num2 = Double.parseDouble(arr[1]);
            res= num1-num2;
        }

        else if(operator==3) {
            String arr[] = expr.split("\\*");
//            Log.i("My_tag", "" + arr[0]);
            double num1 = Double.parseDouble(arr[0]);
            double num2 = Double.parseDouble(arr[1]);
            res= num1*num2;
        }

        else if(operator==4) {
            String arr[] = expr.split("/");
//            Log.i("My_tag", "" + arr[0]);
            double num1 = Double.parseDouble(arr[0]);
            double num2 = Double.parseDouble(arr[1]);
            res= num1/num2;
        }
        else if(flag==1){
            String arr[] = expr.split("\\(");
            String trigo = arr[0];
            String num = arr[1].substring(0,arr[1].length()-1);

            double num1 = Double.parseDouble(num);
            if(trigo.equals("sin")) {
            res=  Math.sin(Math.toRadians(num1));
            }
            else if(trigo.equals("cos")) {
                res=  Math.cos(Math.toRadians(num1));
            }
            else if(trigo.equals("tan")) {
                res=  Math.tan(Math.toRadians(num1));
            }

        }

 return res;
    }
}
