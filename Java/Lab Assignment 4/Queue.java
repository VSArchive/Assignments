import java.util.Scanner;

public class Queue extends StoreData {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue queue = new Queue();

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
                    queue.insert(item);
                    break;
                }
                case 2: {
                    queue.delete();
                    break;
                }
                case 3: {
                    print(queue);
                    break;
                }
            }
        }

        scanner.close();
    }

    public static void print(Queue queue){
        for (int i = queue.ed; i < queue.srt; i++) {
            if(queue.arr[i] != 0){
                System.out.println(queue.arr[i]);
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
        arr[ed] = 0;
        ed++;
    }
}
