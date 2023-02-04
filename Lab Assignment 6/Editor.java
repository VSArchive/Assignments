import java.io.*;

import java.util.Scanner;

public class Editor {
    public static void main(String[] args) {

        String[] prepositions = { "on", "in", "at", "since", "for", "ago", "before", "to", "past", "till", "until",
                "by", "beside", "under", "below", "over", "above", "across", "through", "into", "towards", "onto",
                "from", "of" };

        try {
            FileReader fileReader = new FileReader("paragraph.txt");
            FileWriter fileWriter = new FileWriter("paragraph.txt", true);
            FileWriter summaryWriter = new FileWriter("summary.txt");
            StringBuffer buffer = new StringBuffer();

            int text;
            int vowelCounter = 0;
            int prepositionCounter = 0;
            while ((text = fileReader.read()) != -1) {
                buffer.append((char) text);
                if ((char) text == 'a' || (char) text == 'e' || (char) text == 'i' || (char) text == 'o'
                        || (char) text == 'u') {
                    vowelCounter++;
                }
            }

            String[] arr = buffer.toString().split(" ");

            for (String word : arr) {
                for (String preposition : prepositions) {
                    if (word.equals(preposition)) {
                        prepositionCounter++;
                    }
                }
            }

            summaryWriter.write("Vowels Count : " + vowelCounter);

            summaryWriter.append("\n" + "Preposition Count : " + prepositionCounter);

            summaryWriter.close();

            Scanner scanner = new Scanner(System.in);

            boolean loop = true;

            while (loop) {
                System.out.println("1. Add at end");
                System.out.println("2. Add at specific position");
                System.out.println("3. Edit at specific position");
                System.out.println("4. Delete at specific position");
                System.out.println("5. Print");
                System.out.println("6. Write to File");

                System.out.print("Enter option : ");

                int option = scanner.nextInt();
                scanner.nextLine();

                switch (option) {
                    case 0: {
                        loop = false;
                        break;
                    }
                    case 1: {
                        System.out.print("Enter string to add : ");
                        String word = scanner.nextLine();
                        buffer.append(" " + word);
                        break;
                    }
                    case 2: {
                        System.out.print("Enter index to add : ");
                        int index = scanner.nextInt();
                        scanner.nextLine();
                        System.out.print("Enter string to add : ");
                        String word = scanner.nextLine();
                        buffer.insert(index, " " + word);
                        break;
                    }
                    case 3: {
                        System.out.print("Enter index From : ");
                        int indexFrom = scanner.nextInt();
                        scanner.nextLine();

                        System.out.print("Enter index To : ");
                        int indexTo = scanner.nextInt();
                        scanner.nextLine();

                        System.out.print("Enter string to edit : ");
                        String word = scanner.nextLine();
                        buffer.replace(indexFrom, indexTo, word);
                        break;
                    }
                    case 4: {
                        System.out.print("Enter index From : ");
                        int indexFrom = scanner.nextInt();
                        scanner.nextLine();

                        System.out.print("Enter index To : ");
                        int indexTo = scanner.nextInt();
                        scanner.nextLine();
                        buffer.delete(indexFrom, indexTo);
                        break;
                    }
                    case 5: {
                        System.out.println(buffer);
                        break;
                    }
                    case 6: {
                        fileWriter.append("\n" + buffer.toString());
                        loop = false;
                        fileWriter.close();
                        break;
                    }
                }
            }
            scanner.close();
            fileReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
