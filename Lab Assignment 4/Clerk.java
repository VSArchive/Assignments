import java.util.Scanner;

public class Clerk extends Employee {
    public static void main(String[] args) {
        Clerk clerk = new Clerk();

        clerk.salary(1, "Test");
    }

    @Override
    public void salary(int id, String name){
        super.salary(id, name);

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter basic amount : ");
        basic = scanner.nextInt();
        System.out.print("Enter hra amount : ");
        hra = scanner.nextInt();

        double salary = basic + hra;

        System.out.println(salary);

        scanner.close();
    }

}
