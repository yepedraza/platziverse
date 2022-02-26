package Java;

public class Paypal extends payment{
    String email;

    public Paypal(Integer id, String email){
        super(id);
        this.email = email;
    }
}
