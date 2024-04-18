import static java.lang.Math.*;

import java.util.Arrays;
import java.util.Random;

public class Main {
    public static void main (String[] args){
        //task1. создать одномерный массив long нечетными числами 5..19 включительно в порядке убывания
        int counter = 0;

        for (int i = 5; i < 20; i++){
            if ( i % 2 != 0 ){
                counter += 1;
            }
        }

        long[] arrayA = new long[counter];

        for (int i = 0, j = 19; j >= 5; i++, j -= 2){
            arrayA[i] = j;
        }
        //task2. Создать одномерный массив x типа float. Заполнить его 10-ю случайными числами в диапазоне от -6.0 до 5.0.
        float[] arrayX = new float[10];
        float min = -6.0f;
        float max = 5.0f;
        Random rand = new Random();
        for(int i = 0; i < arrayX.length; i++){
            arrayX[i] = (min + rand.nextFloat() * (max-min));
            //System.out.println(arrayX[i]);
        }
        //task3. Создать двумерный массив a размером 8x10. Вычислить его элементы по следующей формуле (где x = x[j]):
        double[][] arrayResult = new double[8][10]; //i- строка, j - столбец
        for(int i = 0; i < arrayResult.length; i++){
            if(arrayA[i] == 17){
                for(int j = 0; j < arrayResult[i].length; j++){
                   arrayResult[i][j] = asin(sin(log(pow(sin(arrayX[j]),2))));
                }
            } else if ((arrayA[i] == 9) || (arrayA[i] == 11) ||  (arrayA[i] == 15) || (arrayA[i] == 19)){
                for(int j = 0; j < arrayResult[i].length; j++){
                    arrayResult[i][j] = sin(PI*arrayX[j] / 1.0/4);
                }
            }  else {
                Arrays.fill(arrayResult[i], pow((sin(pow(E, (sin(arrayX[i]))))), 1.0 / 3));
            }
        }
        //task4. Напечатать полученный в результате массив в формате с пятью знаками после запятой.
        for (int i = 0; i < arrayResult.length; i++ ){
            for (int j = 0; j < arrayResult[i].length; j++){
                if(arrayResult[i][j] == 1){
                    System.out.format("%10s","######");
                } else
                    System.out.format("%10.5f",arrayResult[i][j]);
            }


            System.out.println();
        }int z[][] = new int[10][];
        z[3] = new int [5];
        z[3][4] = 77;
        System.out.println(z);
    }

}
// если выводит единицу, заменить ее на ###
//jdb > вывести содержание массива arrayX (dump название_массива)

