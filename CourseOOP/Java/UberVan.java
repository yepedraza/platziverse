package Java;

import java.util.ArrayList;
import java.util.Map;

public class UberVan extends EspecialService {   

    public UberVan(String license, account driver, 
    Map<String, Map<String, Integer>> typeCarAccepted, 
    ArrayList<String> seatsMaterial){
        super(license, driver, typeCarAccepted, seatsMaterial);
    }
}