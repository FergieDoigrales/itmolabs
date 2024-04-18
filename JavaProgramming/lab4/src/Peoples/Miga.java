package Peoples;

import Enums.Locations;
import Enums.Times;
import Items.Item;

public class Miga extends Person {
    FixFex fixfex = new FixFex("Фикс и Фекс");

    public Miga(String name) {
        super(name);
    }

    public String whileTalking(String whatHappened) {
        return "Пока " + this.getName() + " говорил, " + whatHappened + " ";
    }

    public String setTogether(Times time) {
        return time.label + " " + this.getName() + " поставил " + fixfex.getName() + " рядышком. ";
    }

    public String makeToDo(Item item) {
        return "Приказав им стоять смирно, " + this.getName() + " треснул каждого по лбу " + item.getName() + ", отчего " + fixfex.fell((Locations.floor));
    }

    public String makeSomeoneToDo(Person julio, Item.SpaceSuit spaceSuit) {
        return this.getName() + " и " + julio.getName() + " велели Незнайке отнести " + spaceSuit.getName() + " в машину, а сами зашли в комнату к Клопсу.";
    }

    class FixFex extends Person {

        public FixFex(String name) {
            super(name);
        }

        public String fell(Locations place) {
            return this.getName() + " тоже свалились " + place.label + ".";
        }
    }
}
