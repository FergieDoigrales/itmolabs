package Peoples;


public class Fix extends Person {

    public Fix(String name) {
        super(name);
    }

    public String go(Enums.Adverbs adverb) {
        return this.getName() + " " + adverb.label + " зашагал по тропинке, ";
    }

    public String move() {
        int opposity = (int) (Math.random() * 6); // с 50% вероятностью персонаж может пошевелиться
        if (opposity > 3)
            return this.getName() + " пошевелился, ";
        else return "";
    }
}
