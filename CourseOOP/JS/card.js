class Card extends Payment{
    constructor(id, number, CVV_number, date){
        super(id)
        this.number = number;
        this.CVV_number = CVV_number;
        this.date = date;
    }
}