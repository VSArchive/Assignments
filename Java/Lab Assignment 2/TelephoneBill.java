import java.util.Scanner;

class Data {
    String phno;
    String name;
    int unitsConsumed;

    Data(String phno, String name, int unitsConsumed) {
        this.phno = phno;
        this.name = name;
        this.unitsConsumed = unitsConsumed;
    }
}

public class TelephoneBill {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        final int hireCharge = 100;
        int billAmount = 0;

        System.out.print("Enter units consumed : ");
        int unitsConsumed = scanner.nextInt();

        Data person = new Data("9390345080", "Vineel Sai", unitsConsumed);
        
        if(person.unitsConsumed > 100){
            billAmount = hireCharge + 100;

            person.unitsConsumed -= - 100;

            if(person.unitsConsumed > 100){
                billAmount += 150;
                person.unitsConsumed -= - 100;

                billAmount += 2 * person.unitsConsumed;

                display(billAmount);
            } else {
                display(billAmount + (1.5 * person.unitsConsumed));
            }
        } else {
            display(hireCharge + person.unitsConsumed);
        }

        scanner.close();
    }

    public static void display(double billAmount) {
        System.out.println(billAmount);
    }
}
