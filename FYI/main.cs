using System;
using static System.Console;



public class main{

    public static void Main(){
        string s = System.Console.ReadLine();
        string[] subs = s.Split(' ');
        
        int product = 1;
        foreach (var sub in subs)
        {
            int int_sub = int.Parse(sub);
            // WriteLine(int_sub);
            
            product = product * int_sub;
        }
        WriteLine(product);
        }     // Main
} // main


