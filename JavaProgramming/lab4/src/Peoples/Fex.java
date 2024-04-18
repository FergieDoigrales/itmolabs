package Peoples;

public class Fex extends Person {
    public Fex(String name) {
        super(name);
    }

    public String appear(Enums.Times time, Enums.Locations location) {
        return time.label + " " + location.label + " выскочил другой слуга господина Клопса -- " + this.getName()
                + ". ";
    }

    public String gagedMouth(Items.Item item) {
        return "Не успел " + this.getName() + " и слова сказать, как руки у него были скрючены, а во рту торчал " + item.getName() + ". ";
    }

    public String move() {
        int opposity = (int) (Math.random() * 6); // с 50% вероятностью персонаж может пошевелиться
        if (opposity > 3)
            return this.getName() + " пошевелился, ";
        else return "";
    }
}
