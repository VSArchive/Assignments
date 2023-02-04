import java.util.Scanner;

public class Manager extends Employee {
    public static void main(String[] args) {
        Manager manager = new Manager();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Name : ");
        String name = scanner.nextLine();

        System.out.print("Enter ID : ");
        int id = scanner.nextInt();

        manager.salary(id, name);

        scanner.close();
    }

    @Override
    public void salary(int id, String name){
        super.salary(id, name);

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter basic amount : ");
        basic = scanner.nextInt();

        double totalSalary = basic + (0.05 * basic) + (0.04 * basic);

        System.out.println(totalSalary);

        scanner.close();
    }

}
