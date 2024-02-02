import java.util.Scanner;

public class factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan Nama Mahasiswa: ");
        String nama = scanner.nextLine();

        System.out.print("Masukkan Nilai Asli: ");
        int nilai_asli = scanner.nextInt();

        System.out.print("Masukkan Durasi: ");
        int durasi = scanner.nextInt();

        double nilai_akhir;

        if (durasi < 60) {
            nilai_akhir = 1.2 * nilai_asli;
        } else if (60 <= durasi && durasi <= 70) {
            nilai_akhir = nilai_asli;
        } else if (70 < durasi && durasi < 90) {
            nilai_akhir = 0.75 * nilai_asli;
        } else if (90 <= durasi && durasi <= 100) {
            nilai_akhir = 0.5 * nilai_asli;
        } else {
            nilai_akhir = 0.2 * nilai_asli;
        }

        System.out.println(nama + " mendapatkan nilai akhir " + nilai_akhir);
    }
}
