import javax.swing.*;
import java.awt.*;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Alphabets {
    public static void main(String[] args) {
        JFrame frame = new JFrame();

        JButton fileChooser = new JButton("Open File Chooser");

        JTextArea textArea = new JTextArea(5, 50);

        JButton vowels = new JButton("Count Vowels");
        JButton consonants = new JButton("Count Consonants");
        JButton punctuations = new JButton("Count Punctuations");
        JButton capitalize = new JButton("Capitalize");

        JLabel answer = new JLabel();

        JCheckBox checkBox = new JCheckBox("Change Color");

        fileChooser.addActionListener(a -> {
            textArea.setText("");
            JFileChooser chooser = new JFileChooser();
            int result = chooser.showSaveDialog(null);
            if (result == JFileChooser.APPROVE_OPTION) {
                try {
                    Scanner scanner = new Scanner(chooser.getSelectedFile());
                    while (scanner.hasNextLine()) {
                        textArea.append(scanner.nextLine());
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            }
        });

        vowels.addActionListener(a -> {
            int vowelsCount = 0;
            for (String alpha : textArea.getText().split("")) {
                if (alpha.toLowerCase().equals("a") || alpha.toLowerCase().equals("e")
                        || alpha.toLowerCase().equals("i") || alpha.toLowerCase().equals("o")
                        || alpha.toLowerCase().equals("u")) {
                    vowelsCount++;
                }
            }
            answer.setText("Vowels Count : " + vowelsCount);
        });

        consonants.addActionListener(a -> {
            int consonantsCount = 0;
            for (String alpha : textArea.getText().split("")) {
                if (!alpha.toLowerCase().equals("a") && !alpha.toLowerCase().equals("e")
                        && !alpha.toLowerCase().equals("i") && !alpha.toLowerCase().equals("o")
                        && !alpha.toLowerCase().equals("u")) {
                    consonantsCount++;
                }
            }
            answer.setText("Consonants Count : " + consonantsCount);
        });

        punctuations.addActionListener(a -> {
            int punctuationsCount = 0;
            for (String alpha : textArea.getText().split("")) {
                if (alpha.toLowerCase().equals(".") || alpha.toLowerCase().equals(",")
                        || alpha.toLowerCase().equals(";") || alpha.toLowerCase().equals("'")) {
                    punctuationsCount++;
                }
            }
            answer.setText("Punctuations Count : " + punctuationsCount);
        });

        capitalize.addActionListener(a -> {
            answer.setText("Capitalized Text : " + textArea.getText().toUpperCase());
        });

        checkBox.addItemListener(a -> {
            if (a.getStateChange() == 1) {
                answer.setForeground(Color.RED);
            } else {
                answer.setForeground(Color.BLACK);
            }
        });

        frame.add(fileChooser);
        frame.add(textArea);
        frame.add(vowels);
        frame.add(consonants);
        frame.add(punctuations);
        frame.add(capitalize);
        frame.add(answer);
        frame.add(checkBox);

        frame.setLayout(new FlowLayout());
        frame.setVisible(true);
        frame.setTitle("Sentence");
        frame.setSize(550, 400);
    }
}
