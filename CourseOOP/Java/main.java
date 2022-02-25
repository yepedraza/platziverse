package Java;

class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");

        car car = new car("AMQ123", new account("Yery Pedraza", "AMQ123"));
        car.passenger = 4;

        // System.out.println("Car License: " + car.license); 
        car.printDataCar(); //Using print method

        car car2 = new car("QWE567", new account("Agusto Agudelo", "QWE567"));
        car2.passenger = 3;

        //System.out.println("Car License: " + car2.license);
        car2.printDataCar(); //Using print method
    }

}