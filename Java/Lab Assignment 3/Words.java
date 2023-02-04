import java.util.ArrayList;
import java.util.Scanner;

class Words {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] input = new String[5];
        ArrayList<String> startWithA = new ArrayList<String>();
        ArrayList<String> startWithE = new ArrayList<String>();
        ArrayList<String> startWithI = new ArrayList<String>();
        ArrayList<String> startWithO = new ArrayList<String>();
        ArrayList<String> startWithU = new ArrayList<String>();

        ArrayList<String> numbers = new ArrayList<String>();

        int vowelCount = 0;

        for(int i = 0; i < 5; i++){
            input[i] = scanner.nextLine();
        }

        int sentenceCount = 0;

        for(String i: input){
            for(String j: i.split(" ")){
                if(j.toLowerCase().startsWith("a")){
                    startWithA.add(j);
                    vowelCount++;
                } else if(j.toLowerCase().startsWith("e")){
                    startWithE.add(j);
                    vowelCount++;
                } else if(j.toLowerCase().startsWith("i")){
                    startWithI.add(j);
                    vowelCount++;
                } else if(j.toLowerCase().startsWith("o")){
                    startWithO.add(j);
                    vowelCount++;
                } else if(j.toLowerCase().startsWith("u")){
                    startWithU.add(j);
                    vowelCount++;
                }

                j = j.replaceAll("[*a-zA-Z]", "").trim();

                if(!j.isEmpty()){
                    numbers.add(j);
                }
            }

            sentenceCount++;

            System.out.print("Sentence " + sentenceCount + " : ");

            for (String num : numbers) {
                System.out.print(num + ",");
            }

            System.out.println("\n");

            numbers.clear();
        }

        System.out.println("No of Words Starting with Vowels : " + vowelCount + "\n");

        System.out.print("A : ");
        for (String word : startWithA) {
            System.out.print(word + ", ");
        }
        System.out.println("\n");

        System.out.print("E : ");
        for (String word : startWithE) {
            System.out.print(word + ", ");
        }
        System.out.println("\n");

        System.out.print("I : ");
        for (String word : startWithI) {
            System.out.print(word + ", ");
        }
        System.out.println("\n");

        System.out.print("O : ");
        for (String word : startWithO) {
            System.out.print(word + ", ");
        }
        System.out.println("\n");

        System.out.print("U : ");
        for (String word : startWithU) {
            System.out.print(word + ", ");
        }
        System.out.println("\n");

        scanner.close();
        
    }
}