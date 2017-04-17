package com.example.sanika.calci;

import android.content.Context;
import android.content.SharedPreferences;

/**
 * Created by Sanika on 17-Apr-17.
 */

public class MemorySaveRecall {
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    public static  String DATA = "RESULT";
    public static  String PREF_NAME = "MEMORY_PREF";
    Context context;
    public MemorySaveRecall(Context context){
        this.context  = context;
        pref =  context.getSharedPreferences(PREF_NAME,Context.MODE_PRIVATE);
        editor = pref.edit();
    }
    void saveResult(String res){
        editor.putString(DATA,res);
        editor.commit();
    }

    String recallResult(){
        return  pref.getString(DATA,"0");

    }

}

