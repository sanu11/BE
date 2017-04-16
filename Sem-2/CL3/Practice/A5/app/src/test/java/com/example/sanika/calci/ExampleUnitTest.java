package com.example.sanika.calci;

import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() throws Exception {
        assertEquals(5.0, MainActivity.calculate("2+3",1,0),0);
    }
    @Test
    public void subtraction_isCorrect() throws Exception {
        assertEquals(-1, MainActivity.calculate("2-3",2,0),0);
    }
    @Test
    public void multiplication_isCorrect() throws Exception {
        assertEquals(6, MainActivity.calculate("2*3",3,0),0);
    }
    @Test
    public void division_isCorrect() throws Exception {
        assertEquals(2,MainActivity.calculate("4/2",4,0),0);
    }
    @Test
    public void sin_isCorrect() throws Exception {
        assertEquals(0.5,MainActivity.calculate("sin(30)",0,1),0);
    }
    @Test
    public void cos_isCorrect() throws Exception {
        assertEquals(1.0,MainActivity.calculate("cos(0)",0,1),0);
    }
    @Test
    public void tan_isCorrect() throws Exception {
        assertEquals(0.0,MainActivity.calculate("tan(0)",0,1),0);
    }


}
