import java.util.*;


public class STRAT3 {
    int n;
    int m;
    int [][] houses;
    STRAT3(){
        takeInput();
    }
    private void takeInput(){

        System.out.println("Give ALREADY SORTED input for Strat3: ");
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
        PriorityQueue<int []> pq = new PriorityQueue<>(new Comparator<>(){
            @Override
            public int compare(int a[], int b[]) {
                return ((a[1]-a[0]) - (b[1]-b[0]));
            }
        });
        List<Integer> optimalset = new ArrayList<>();
        int day = 1;
        int house_num = 0;
        while(day<=n && house_num<=m){
            //add all compatible job to the PQ for ongoing day
            while(house_num<m && houses[house_num][0]<=day){
                int [] interval = new int[3];
                interval[0] = houses[house_num][0];
                interval[1] = houses[house_num][1];
                interval[2] = ++house_num;
                pq.add(interval);
            }
            //once added then try to get the first compatible interval among the ones available
            //possible no new houses are compatible with the day so we try to schedule any other house
            //so we poll the houses available untill a compatible one is found or we exaust all the available houses

            while(!pq.isEmpty() && pq.peek()[1]<day){
                pq.poll();
            }
            if(!pq.isEmpty()){
                //upon finding a compatible house, schedule it and note the day
                int [] house_TBS = pq.poll();
                if(house_TBS[1]>=day){
                    optimalset.add(house_TBS[2]);
                }
            }
            day++;

        }
        return  optimalset;
    }
    public static void main(String args[]){
        STRAT3 strat3 = new STRAT3();
        List<Integer> optimal_Strat3 = strat3.optimize();
        System.out.println(optimal_Strat3.toString());
    }
}
