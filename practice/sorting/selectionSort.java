package practice.sorting;

import java.util.Arrays;

public class selectionSort {
    public static void main(String[] args) {
        int[] array = {12, 5, 46, 8, 1, 4, 100};
        sort(array);
        System.out.println("Sorted array: " + Arrays.toString(array));

    }

    static void sort(int[] array) {
        int length = array.length;

        for (int i = 0; i < length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }

            }
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
    }
}
