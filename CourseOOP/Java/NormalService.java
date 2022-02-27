package Java;

public class NormalService extends car{
    String brand;
    String model;

    public NormalService(String license, account driver, String brand, String model){
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }

}
