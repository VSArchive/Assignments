import java.util.Scanner;
import java.lang.Math;

public class AreaPerimeter {
    public static void main(String[] args) {

        AreaPerimeter ap = new AreaPerimeter();

        while(true){
            
            Scanner s = new Scanner(System.in);

            System.out.println("1. Triangle");
            System.out.println("2. Rectangle");
            System.out.println("3. Square");
            System.out.println("4. Circle");

            int option = s.nextInt();

            switch (option){
                case 1: {
                    System.out.print("Enter length of side : ");
                    int side = s.nextInt();

                    double ratio = ap.Triangle(side);

                    ap.display(ratio);

                    break;
                }

                case 2: {
                    System.out.print("Enter length of side : ");
                    int length = s.nextInt();

                    System.out.print("Enter bredth of side : ");
                    int bredth = s.nextInt();

                    double ratio = ap.Rectangle(length, bredth);

                    ap.display(ratio);

                    break;
                }

                case 3: {
                    System.out.print("Enter length of side : ");
                    int side = s.nextInt();

                    double ratio = ap.Square(side);

                    ap.display(ratio);
                    break;
                }

                case 4: {
                    System.out.print("Enter radius of circle : ");
                    int radius = s.nextInt();

                    double ratio = ap.Circle(radius);

                    ap.display(ratio);
                    break;
                }
            }
        }
        
    }

    void display(Double ratio){
        System.out.println("Ratio is " + ratio);
    }

    double Triangle(int side){
        double area = Math.pow(3.0, 1/2) * side * side / 2;
        int perimeter = 3 * side;
        return area/perimeter;
    }

    double Rectangle(int length, int bredth){
        double area = length * bredth;
        int perimeter = 2 * (length + bredth);
        return area/perimeter;
    }

    double Square(int side){
        double area = side * side;
        int perimeter = 4 * side;
        return area/perimeter;
    }

    double Circle(int radius){
        double area = 3.14 * radius * radius;
        double perimeter = 2 * 3.14 * radius;
        return area/perimeter;
    }

}
