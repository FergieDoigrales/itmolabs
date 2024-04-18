package Peoples;

import Enums.Locations;
import Enums.Times;
import Items.Item;

public class Julio extends Person implements seeing {
    public Julio(String name) {
        super(name);
    }
    public String tieSomeOne(Person person, Item item) {
        return this.getName() + " опутал веревкой " + person.getName() + "а, словно паук паутиной, привязал его крепко-накрепко к "
                + item.getName() + "у" + " и заткнул рот затычкой.";
    }

    public String saw(String whatSee, Item item) {
        return "Увидев, что " + whatSee + ", " + this.getName() + " ткнул его " + item.getName() + " в темя.";
    }

    public String gagMouth(Times time) {
        return "Больше он ничего не успел сказать, так как " + this.getName() + " " + time.label + " заткнул ему рот кляпом. ";
    }

    public String goOut(Person person, Locations location, Item.SpaceSuit item) {
        return person.getName() + " и " + this.getName() + " вышли " + location.label + " и, позвав Незнайку, отправились искать " + item.getName() + ".";
    }
}
