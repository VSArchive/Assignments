import java.util.Scanner;

class Currency{

    String currencyCode;
    String currencyName;
    double exchangeRate;

    Currency(){
        currencyCode = "USD";
        currencyName = "Doller";
        exchangeRate = 70.32;
    }

    Currency(String currencyCode, String currencyName, double exchangeRate){
        this.currencyCode = currencyCode;
        this.currencyName = currencyName;
        this.exchangeRate = exchangeRate;
    }
}

class CurrencyCalc {
    public static void main(String[] args) {

        CurrencyCalc currencyCalc = new CurrencyCalc();

        Scanner scanner = new Scanner(System.in);

        System.out.println("From Currency");
        System.out.print("Enter Curency Code : ");
        String fromCurrencyCode = scanner.nextLine();
        System.out.print("Enter Curency Name : ");
        String fromCurrencyName = scanner.nextLine();
        System.out.print("Enter Exchange Rate to INR : ");
        double fromExchangeRate = Double.parseDouble(scanner.nextLine());

        System.out.println("To Currency");
        System.out.print("Enter Curency Code : ");
        String toCurrencyCode = scanner.nextLine();
        System.out.print("Enter Curency Name : ");
        String toCurrencyName = scanner.nextLine();
        System.out.print("Enter Exchange Rate to INR : ");
        double toExchangeRate = Double.parseDouble(scanner.nextLine());

        Currency from = new Currency(fromCurrencyCode, fromCurrencyName, fromExchangeRate);
        Currency to = new Currency(toCurrencyCode, toCurrencyName, toExchangeRate);

        System.out.print("No Of Currency to Exchange : ");
        int currencyCount = scanner.nextInt();

        currencyCalc.calc(from, to, currencyCount);

        scanner.close();
    }

    public void calc(Currency from, Currency to, int count){
        double cost = to.exchangeRate / from.exchangeRate;

        System.out.println("Inr required to buy : " + cost * count * from.exchangeRate);
    }
}
