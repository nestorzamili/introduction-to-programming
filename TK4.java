import java.util.Scanner;
import java.util.Random;

public class TK4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        int menu, batasBawah, batasAtas, temp, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w;
        int[] data = new int[5];
        boolean ulang = true;

        while (ulang) {
            System.out.println("Menu Pilihan");
            System.out.println("1. Random Data");
            System.out.println("2. Simulasi Bubble Sort - Ascending");
            System.out.println("3. Simulasi Selection Sort - Ascending");
            System.out.println("4. Simulasi Bubble Sort - Descending");
            System.out.println("5. Simulasi Selection Sort - Descending");
            System.out.println("6. Keluar");
            System.out.print("Masukkan pilihan anda : ");
            menu = input.nextInt();

            switch (menu) {
                case 1:
                    System.out.print("Masukkan batas bawah : ");
                    batasBawah = input.nextInt();
                    System.out.print("Masukkan batas atas : ");
                    batasAtas = input.nextInt();
                    for (i = 0; i < data.length; i++) {
                        data[i] = rand.nextInt(batasAtas - batasBawah + 1) + batasBawah;
                    }
                    System.out.println("Data yang dihasilkan : ");
                    for (i = 0; i < data.length; i++) {
                        System.out.print(data[i] + " ");
                    }
                    System.out.println();
                    break;
                case 2:
                    System.out.println("Data yang dihasilkan : ");
                    for (i = 0; i < data.length; i++) {
                        System.out.print(data[i] + " ");
                    }
                    System.out.println();
                    for (i = 0; i < data.length - 1; i++) {
                        for (j = 0; j < data.length - 1; j++) {
                            if (data[j] > data[j + 1]) {
                                temp = data[j];
                                data[j] = data[j + 1];
                                data[j + 1] = temp;
                            }
                        }
                        System.out.print("Putaran " + (i + 1) + " : ");
                        for (k = 0; k < data.length; k++) {
                            System.out.print(data[k] + " ");
                        }
                        System.out.println();
                    }
                    break;
                case 3:
                    System.out.println("Data yang dihasilkan : ");
                    for (i = 0; i < data.length; i++) {
                        System.out.print(data[i] + " ");
                    }
                    System.out.println();
                    for (i = 0; i < data.length - 1; i++) {
                        for (j = i + 1; j < data.length; j++) {
                            if (data[i] > data[j]) {
                                temp = data[i];
                                data[i] = data[j];
                                data[j] = temp;
                            }
                        }
                        System.out.print("Putaran " + (i + 1) + " : ");
                        for (k = 0; k < data.length; k++) {
                            System.out.print(data[k] + " ");
                        }
                        System.out.println();
                    }
                    break;
                case 4:
                    System.out.println("Data yang dihasilkan : ");
                    for (i = 0; i < data.length; i++) {
                        System.out.print(data[i] + " ");
                    }
                    System.out.println();
                    for (i = 0; i < data.length - 1; i++) {
                        for (j = 0; j < data.length - 1; j++) {
                            if (data[j] < data[j + 1]) {
                                temp = data[j];
                                data[j] = data[j + 1];
                                data[j + 1] = temp;
                            }
                        }
                        System.out.print("Putaran " + (i + 1) + " : ");
                        for (k = 0; k < data.length; k++) {
                            System.out.print(data[k] + " ");
                        }
                        System.out.println();
                    }
                    break;
                case 5:
                    System.out.println("Data yang dihasilkan : ");
                    for (i = 0; i < data.length; i++) {
                        System.out.print(data[i] + " ");
                    }
                    System.out.println();
                    for (i = 0; i < data.length - 1; i++) {
                        for (j = i + 1; j < data.length; j++) {
                            if (data[i] < data[j]) {
                                temp = data[i];
                                data[i] = data[j];
                                data[j] = temp;
                            }
                        }
                        System.out.print("Putaran " + (i + 1) + " : ");
                        for (k = 0; k < data.length; k++) {
                            System.out.print(data[k] + " ");
                        }
                        System.out.println();
                    }
                    break;
                case 6:
                    ulang = false;
                    break;
                default:
                    System.out.println("Pilihan tidak tersedia");
                    break;
            }
        }
    }
}