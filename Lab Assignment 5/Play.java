import java.util.ArrayList;
import java.util.Scanner;

public class Play implements Game {
    public static void main(String[] args) {
        Play play = new Play();

        Scanner scanner = new Scanner(System.in);

        System.out.println("1. FootBall");
        System.out.println("2. BasketBall");
        System.out.println("3. Cricket");

        System.out.print("Enter Option : ");
        int option = scanner.nextInt();

        if (option == 1){
            play.playGame("FootBall");
        } else if (option == 2){
            play.playGame("BasketBall");
        } else if (option == 3){
            play.playGame("Cricket");
        }

        scanner.close();
    }

	public void playGame(String game) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Name : ");
        String name = scanner.nextLine();

        System.out.print("Enter No of Games Played : ");
        String gamesPlayed = scanner.nextLine();
        
        System.out.print("Enter points scored : ");
        String points = scanner.nextLine();

        System.out.print("Enter No of Wins : ");
        String wins = scanner.nextLine();

        ArrayList<String> statistics = new ArrayList<>();

        statistics.add(gamesPlayed);
        statistics.add(points);
        statistics.add(wins);

        if (game == "FootBall"){
            FootBall footBall = new FootBall();

            footBall.setName(name);

            footBall.setStatistics(statistics);

            System.out.println(footBall.getName());
            System.out.println("Ratio of " + footBall.getStatistics().get(2) + " : " + footBall.getStatistics().get(0));
            System.out.println("Ratio of matches won : " + footBall.getStatistics().get(1));

        } else if (game == "BasketBall") {
            BasketBall basketBall = new BasketBall();
            basketBall.setName(name);

            basketBall.setStatistics(statistics);

            System.out.println(basketBall.getName());
            System.out.println("Ratio of " + basketBall.getStatistics().get(2) + " : " + basketBall.getStatistics().get(0));
            System.out.println("Ratio of matches won : " + basketBall.getStatistics().get(1));

        } else if (game == "Cricket") {
            Cricket cricket = new Cricket();
            cricket.setName(name);

            cricket.setStatistics(statistics);

            System.out.println(cricket.getName());
            System.out.println("Ratio of " + cricket.getStatistics().get(2) + " : " + cricket.getStatistics().get(0));
            System.out.println("Ratio of matches won : " + cricket.getStatistics().get(1));
        }

        scanner.close();
	}
}
