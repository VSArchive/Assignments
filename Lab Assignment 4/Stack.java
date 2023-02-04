import java.util.Scanner;

public class Stack extends StoreData {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack stack = new Stack();

        int option = 0;

        while(option != -1){
            System.out.println("1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Print");

            System.out.print("Enter option : ");
            
            option = scanner.nextInt();

            switch(option){
                case 1: {
                    int item;
                    System.out.print("Enter num to insert : ");
                    item = scanner.nextInt();
                    stack.insert(item);
                    break;
                }
                case 2: {
                    stack.delete();
                    break;
                }
                case 3: {
                    print(stack.arr);
                    break;
                }
            }
        }

        scanner.close();
    }

    public static void print(int[] arr){
        for (int i : arr) {
            if(i != 0){
                System.out.println(i);
            }
        }
    }

    @Override
    public void insert(int item){
        arr[srt] = item;
        srt++;
    }

    @Override
    public void delete(){
        srt--;
        arr[srt] = 0;
    }
}
