package practice.binary_search;

import java.util.Arrays;
import java.util.Scanner;

public class binarySearch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter size of the array: ");
        int size = scanner.nextInt();
        int[] array = new int[size];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }
        sort(array);
        System.out.println("Sorted array: " + Arrays.toString(array));

        System.out.println("Enter a key: ");
        int key = scanner.nextInt();
        int low = 0;
        int high = array.length - 1;

        int index = binarySearch(array, key, low, high);

        if (index != -1) {
            System.out.println("Element found at index: " + index);
        } else {
            System.out.println("Element not found in the array.");
        }

        scanner.close();
    }

    static void sort(int[] array) {
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

    static int binarySearch(int[] array, int key, int low, int high) {
        while (low <= high) {
            int mid = (low + high) / 2;
            if (array[mid] == key) {
                return mid;
            } else if (array[mid] < key) {
                low = mid + 1;
            } else high = mid - 1;
        }
        return -1;
    }
}
