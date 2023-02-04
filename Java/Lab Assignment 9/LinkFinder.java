import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.swing.*;
import java.awt.*;

class LinkFinder {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JButton fileChooser = new JButton("Open File Chooser");
        JLabel resultLabel = new JLabel();

        fileChooser.addActionListener(a -> {
            String content = "";
            JFileChooser chooser = new JFileChooser("C:\\Users\\Vineel\\Desktop\\Lab\\Java\\Lab Assignment 9");
            int result = chooser.showSaveDialog(null);
            if (result == JFileChooser.APPROVE_OPTION) {
                try {
                    Scanner scanner = new Scanner(chooser.getSelectedFile());
                    while (scanner.hasNextLine()) {
                        content += scanner.nextLine().trim();
                    }
                    Pattern pattern = Pattern
                            .compile("(http|https)://[a-zA-Z0-9]*\\.?[a-zA-Z0-9]*\\.[a-z]*/?[a-zA-Z0-9]*");
                    Matcher matcher = pattern.matcher(content);
                    while (matcher.find()) {
                        resultLabel.setText(resultLabel.getText() + "           " + matcher.group());
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            }
        });

        frame.add(fileChooser);
        frame.add(resultLabel);

        frame.setLayout(new FlowLayout());
        frame.setVisible(true);
        frame.setTitle("Link Finder");
        frame.setSize(400, 400);
    }
}