package practice.sorting;

import java.util.Arrays;

public class bubbleSort {
    public static void main(String[] args) {
        int[] array = {12, 5, 46, 8, 1, 4, 100};
        sorting(array);
        System.out.println("Sorted array: " + Arrays.toString(array));
    }

    public static void sorting(int[] array) {
        int length = array.length;

        for (int i = 0; i < length; i++) {
            for (int j = 1; j < length - i; j++) {
                if (array[j - 1] > array[j]) {
                    int temp = array[j];
                    array[j] = array[j - 1];
                    array[j - 1] = temp;
                }
            }
        }
    }
}