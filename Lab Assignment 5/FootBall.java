import java.util.ArrayList;

public class FootBall implements Player {

    private String name = "";
    private ArrayList<String> statistics = new ArrayList<>();

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
        this.name = name;
	}

	public ArrayList<String> getStatistics() {
		ArrayList<String> statsCalculated = new ArrayList<>();

        statsCalculated.add(String.valueOf(Double.parseDouble(this.statistics.get(1)) / Double.parseDouble(this.statistics.get(0))));

        statsCalculated.add(String.valueOf(Double.parseDouble(this.statistics.get(2)) / Double.parseDouble(this.statistics.get(0))));

        statsCalculated.add("Goals");

		return statsCalculated;
	}

	public void setStatistics(ArrayList<String> statistics) {
		this.statistics = statistics;
	}
    
}
