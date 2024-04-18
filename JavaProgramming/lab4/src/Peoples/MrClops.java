package Peoples;

import Enums.Locations;
import Enums.Times;
import Items.Item;

public class MrClops extends Person implements drinking {

    public MrClops(String name) {
        super(name);
    }

    public String sit(Locations location, Times time) {
        return "Сам " + this.getName() + " сидел " + time.label + " " + location.label + ".";
    }

    public String drink(Item dinkr, Item container) {
        return this.getName() + " попивал " + dinkr.getName() + " из " + container.getName() + ".";
    }

    public String see() {
        class ThreeCops extends Person {
            public ThreeCops(String name) {
                super(name);
            }

            public String enter(Locations location) {
                return this.getName() + " ввалились в " + location.label
                        + ", а вместе с ними Фикс и Фекс со связанными руками и заткнутыми ртами. ";
            }
        }
        ThreeCops threeCops = new ThreeCops("трое полицейских");
        return "и он увидел, как " + threeCops.enter(Locations.room);
    }

    public String spoiledCocoa(Item item, Item item2) {
        return this.getName() + " широко раскрыл рот и опрокинул " + item.getName() + " с горячим " + item2.getName() + " прямо себе на брюки. ";
    }

    public String tryingStand() {
        return this.getName() + " все же болтает ногами и пытается встать";
    }

    public String fall(Item item) {
        return "В результате " + this.getName() + " полетел на пол вместе со " + item.getName() + "ом.";
    }

    public String move() {
        int opposity = (int) (Math.random() * 6); // с 50% вероятностью персонаж может пошевелиться
        if (opposity > 3)
            return this.getName() + " пошевелился, ";
        else return "";
    }
}
