import java.util.Random;
import java.util.Scanner;
//Also can use import java.util.* to import all
public class App {
    //Our magic 8 ball is a simple program that allows the user to input a yes or no question,
    //and calls from an array of answers using a random number to predict our future. 
    public static void main(String[] args) throws Exception {
        while (true) { //Makes our code run forever.
        Scanner scan = new Scanner(System.in); //Initalize Scanner to scan object
        System.out.println("Enter your Yes or No question");
        String s = scan.nextLine(); //Scanner allows the user to enter information to a variable for later use
        Random rand = new Random(); //Initialize class Random to rand object
        int randomNumber = rand.nextInt(8); //Gives us random number 0-7.
        String [] options = {"It is Certain", "Without a doubt", "Signs point to yes", "Maybe", "Ask again later", "Don't count on it", "Very doubtful", "No Bozo"};
        System.out.println(options[randomNumber]);  //Print out random answer from array
        }
        }

    }

