package Java;

import java.util.Date;

public class Card extends payment{
    Integer number;
    Integer CVV_number;
    Date date;

    public Card(Integer id, Integer number, Integer CVV_number, Date date){
        super(id);
        this.number = number;
        this.CVV_number = CVV_number;
        this.date = date;
    }
}
