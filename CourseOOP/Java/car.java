package Java;

public class car {
    private Integer id;
    private String license;
    private account driver;
    private Integer passenger;

    public car(String license, account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar(){
        System.out.println("Car License: " + license + " Name Driver: " + driver.name + " Passengers: " + passenger);
    }

    public Integer getPassenger(){
        return passenger;
    }

    public void setPassenger(Integer passenger){
        if(passenger == 4){
            this.passenger = passenger;
        }
        else{
            System.out.println("Data dennied!");
        }
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public account getDriver() {
        return driver;
    }

    public void setDriver(account driver) {
        this.driver = driver;
    }

    
}
