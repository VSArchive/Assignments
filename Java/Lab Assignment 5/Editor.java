import java.util.Scanner;

public class Editor {
    public static void main(String[] args) {
        StringBuffer buffer = new StringBuffer("Define a class Editor that can edit existing sentences");

        Scanner scanner = new Scanner(System.in);

        boolean loop = true;

        while(loop) {
            System.out.println("1. Add at end");
            System.out.println("2. Add at specific position");
            System.out.println("3. Edit at specific position");
            System.out.println("4. Delete at specific position");
            System.out.println("5. Print");

            System.out.print("Enter option : ");

            int option = scanner.nextInt();
            scanner.nextLine();

            switch(option){
                case 0: {
                    loop = false;
                    break;
                }
                case 1: {
                    System.out.print("Enter string to add : ");
                    String word = scanner.nextLine();
                    buffer.append(" "+word);
                    break;
                }
                case 2: {
                    System.out.print("Enter index to add : ");
                    int index = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Enter string to add : ");
                    String word = scanner.nextLine();
                    buffer.insert(index, " "+word);
                    break;
                }
                case 3: {
                    System.out.print("Enter index to edit : ");
                    int index = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Enter string to edit : ");
                    String word = scanner.nextLine();
                    buffer.replace(index, index, word);
                    break;
                }
                case 4: {
                    System.out.print("Enter index to add : ");
                    int index = scanner.nextInt();
                    scanner.nextLine();
                    buffer.delete(index, index+1);
                    break;
                }
                case 5: {
                    System.out.println(buffer);
                }
            }
        }

        scanner.close();
    }
}
