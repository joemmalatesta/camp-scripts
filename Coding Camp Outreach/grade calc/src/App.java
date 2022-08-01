//I didn't teach this one, but one of the students, while going over the basics, came up with this idea
//and began to implement it. I wrote a script of my own to show how he could make it more interactive
//and fit more use cases. 

//breaking it down to general steps, the program takes a variable amount of test grades, calculates
//and saves the average of them all. It then checks if the average grade was over 80.
//if the grade average is below 80, it allows you to complete math questions, incrementing the grade by
// 3 for each correct answer, until your grade reaches 80.



import java.util.Scanner;
import java.util.Random;
public class App {
    public static void main(String[] args) throws Exception {
        int gradeTotal = 0;
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        System.out.println("How many grades do you want to enter?");
        int numberOfGrades = scan.nextInt();
        int [] grades = new int[numberOfGrades];
        for (int x = 0; x < grades.length; x++ ) {
            System.out.println("Enter grade #" + (x+1));
            int grade = scan.nextInt();
            gradeTotal += grade;
            grades[x] = grade;
        }

        int avgGrade = gradeTotal / grades.length;
        System.out.println("Your Average Grade is ");
        System.out.println(avgGrade);

        while (avgGrade < 80){
            int num1 = rand.nextInt(100);
            int num2 = rand.nextInt(100);
            int answer = num1 + num2;
            System.out.println("What is " + num1 + " + " + num2 + "?");
            int yourAnswer = scan.nextInt();
            if (yourAnswer == answer) {
                avgGrade += 3;
                System.out.println("Your grade is now " + avgGrade);
            }
            else{
                System.out.println("Stupid boy, you will never be smart enough!");
                avgGrade = 0;
                System.out.println("Your grade is now " + avgGrade);
            }
        }
        System.out.println("Congrats, you passed");
        }

    }

