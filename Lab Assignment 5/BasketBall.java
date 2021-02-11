import java.util.ArrayList;

public class BasketBall extends FootBall {

    private String name = "";
    private ArrayList<String> statistics = new ArrayList<>();

    @Override
    public String getName() {
		return this.name;
	}

    @Override
	public void setName(String name) {
        this.name = name;
	}

    @Override
    public ArrayList<String> getStatistics() {
		ArrayList<String> statsCalculated = new ArrayList<>();

        statsCalculated.add(String.valueOf(Double.parseDouble(this.statistics.get(1)) / Double.parseDouble(this.statistics.get(0))));

        statsCalculated.add(String.valueOf(Double.parseDouble(this.statistics.get(2)) / Double.parseDouble(this.statistics.get(0))));

        statsCalculated.add("Goals in Basket Ball");

		return statsCalculated;
	}

    @Override
	public void setStatistics(ArrayList<String> statistics) {
		this.statistics = statistics;
	}
}
