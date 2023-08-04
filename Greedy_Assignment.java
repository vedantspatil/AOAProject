
import java.util.List;

public class Greedy_Assignment{

    public static void main(String[] args) {

        STRAT1 strat1 = new STRAT1();
        List<Integer> optimal_Strat1 = strat1.optimize();
        System.out.println(optimal_Strat1.toString());

        STRAT2 strat2 = new STRAT2();
        List<Integer> optimal_Strat2 = strat2.optimize();
        System.out.println(optimal_Strat2.toString());

        STRAT3 strat3 = new STRAT3();
        List<Integer> optimal_Strat3 = strat3.optimize();
        System.out.println(optimal_Strat3.toString());

        STRAT4 strat4 = new STRAT4();
        List<Integer> optimal_Strat4 = strat4.optimize();
        System.out.println(optimal_Strat4.toString());


    }


}
