package Java;

class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");

        car car = new car();
        car.license = "AMQ123";
        car.driver = "Yery Pedraza";
        car.passenger = 4;

        System.out.println("Car License: " + car.license);

        car car2 = new car();
        car2.license = "QWE567";
        car2.driver = "Agusto Agudelo";
        car2.passenger = 3;

        System.out.println("Car License: " + car2.license);
    }

}