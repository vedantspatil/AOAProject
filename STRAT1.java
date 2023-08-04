import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class STRAT1 {
    // O(n) implementation to assign jobs on n days out of the m available ones
    int n;
    int m;
    int [][] houses;
    STRAT1(){
        takeInput();
    }
    private void takeInput(){

        System.out.println("Give ALREADY SORTED input for Strat1: ");
        Scanner sc = new Scanner(System.in);
        String nm = sc.nextLine();
        int n = Integer.valueOf(nm.split(" ")[0]);
        int m = Integer.valueOf(nm.split(" ")[1]);
        this.n = n;
        this.m = m;
        this.houses = new int[m][2];
        for(int i=0; i<m; i++){
            String duration = sc.nextLine();
            int start = Integer.valueOf(duration.split(" ")[0]);
            int end = Integer.valueOf(duration.split(" ")[1]);
            this.houses[i][0] = start;
            this.houses[i][1] = end;
        }
        //this.printhouses();
    }
    private void printhouses(){
        for (int i=0; i<this.m; i++){
            System.out.println(Arrays.toString(this.houses[i]));
        }
    }

    public List<Integer> optimize(){
        List<Integer> optimalset = new ArrayList<>();
        int day = 1;
        int house_num = 0;
        while(day<=n && house_num<=m){
            //if house eligible on the day then schedule
            if(day>=houses[house_num][0] && day<=houses[house_num][1]){
                optimalset.add(++house_num);
                day++;
            }else{
                if(day<houses[house_num][0]){
                    day++;
                }
                else{
                    house_num++;
                }
            }
        }
        return  optimalset;
    }
    public static void main(String args[]){
        STRAT1 strat1 = new STRAT1();
        List<Integer> optimal_Strat1 = strat1.optimize();
        System.out.println(optimal_Strat1.toString());
    }
}
