package Java;

import java.util.ArrayList;
import java.util.Map;

public class UberBlack extends EspecialService {   

    public UberBlack(String license, account driver, 
    Map<String, Map<String, Integer>> typeCarAccepted, 
    ArrayList<String> seatsMaterial){
        super(license, driver, typeCarAccepted, seatsMaterial);
    }
}