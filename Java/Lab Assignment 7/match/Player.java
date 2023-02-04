package match;

import java.util.ArrayList;

public interface Player {
    String getName();

    void setName(String name);

    ArrayList<String> getStatistics();

    void setStatistics(ArrayList<String> statistics);
}