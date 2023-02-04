public class Validate {
    public static void main(String[] args) {
        System.out.println("First Name : " + args[0]);
        System.out.println("Last Name : " + args[1]);

        String[] dob = args[2].split("/");
        boolean dobError = false;

        if (Integer.parseInt(dob[0]) > 31){
            dobError = true;
        } else if (Integer.parseInt(dob[0]) > 28) {
            if (Integer.parseInt(dob[1]) == 2) {
                if (Integer.parseInt(dob[2]) % 4 != 0 && Integer.parseInt(dob[0]) != 29){
                    dobError = true;
                }
            }
        } if (Integer.parseInt(dob[1]) > 12) {
            dobError = true;
        }

        if (dobError){
            System.out.println("Date of Birth : Please enter a valid date");
        } else {
            calcDate(dob);
        }

        String email = args[3];
        String domain = email.split("@")[1];

        if(domain.contains(".")){
            System.out.println("Domain Name : " + domain);
        } else {
            System.out.println("Domain Name : Please enter a valid mail id");
        }
        
    }

    public static void calcDate(String[] dob){
        String month = "";

        if(Integer.parseInt(dob[1]) == 1){
            month = "January";
        } else if(Integer.parseInt(dob[1]) == 2){
            month = "February";
        } else if(Integer.parseInt(dob[1]) == 3){
            month = "March";
        } else if(Integer.parseInt(dob[1]) == 4){
            month = "April";
        } else if(Integer.parseInt(dob[1]) == 5){
            month = "May";
        } else if(Integer.parseInt(dob[1]) == 6){
            month = "June";
        } else if(Integer.parseInt(dob[1]) == 7){
            month = "July";
        } else if(Integer.parseInt(dob[1]) == 8){
            month = "August";
        } else if(Integer.parseInt(dob[1]) == 9){
            month = "September";
        } else if(Integer.parseInt(dob[1]) == 10){
            month = "October";
        } else if(Integer.parseInt(dob[1]) == 11){
            month = "November";
        } else if(Integer.parseInt(dob[1]) == 12){
            month = "December";
        }

        System.out.println("Date of Birth : " + dob[0] + "-" + month + "-" + dob[2]);
    }
}
