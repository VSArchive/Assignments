public class DisplayWelcome {
    public static void main(String[] args) {
        DisplayWelcome dw = new DisplayWelcome();

        dw.display("Welcome");
    }

    void display(String message){
        System.out.println(message);
    }
}
