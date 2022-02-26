package Java;

class Main{
    public static void main(String[] args) {

        car car = new car("AMQ123", new account("Yery Pedraza", "AMQ123"));
        //car.passenger = 4;

        // System.out.println("Car License: " + car.license); 
        car.printDataCar(); //Using print method

        UberX uberX = new UberX("QWE567", new account("Agusto Agudelo", "QWE567"), "Chevrolet", "Sonic");
        uberX.setPassenger(3);

        //System.out.println("Car License: " + car2.license);
        uberX.printDataCar(); //Using print method
    }

}