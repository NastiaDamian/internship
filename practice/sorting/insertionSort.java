package practice.sorting;

import java.util.Arrays;

public class insertionSort {
    public static void main(String[] args) {
        int[] array = {12, 5, 46, 15, 8, 1, 4, 21};
        sort(array);
        System.out.println("Sorted array: " + Arrays.toString(array));
    }

    static void sort(int[] array) {
        int length = array.length;

        for (int i = 1; i < length; i++) {
            int key = array[i];
            int j = i - 1;

            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }
}
