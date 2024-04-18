package Peoples;

import Items.Item;

import java.util.Objects;

public class Julio extends Person implements seeing{
    public Julio(String name) {
        super(name);
    }
    public String tieSomeOne(Person person, Item item){
        return this.getName() + " опутал веревкой " + person.getName() + ", словно паук паутиной, привязал его крепко-накрепко к "
                + item.getName() + "у" + " и заткнул рот затычкой.";
    }
    public String saw(String whatSee, Item item){
        return "Увидев, что " + whatSee + ", " + this.getName() + " ткнул его " + item.getName() + " в темя.";
    }
    @Override
    public boolean equals(Object otherObj) {
        if (this == otherObj) return true;
        if (otherObj == null) return false;
        if (!this.getClass().equals(otherObj.getClass())) return false;
        Julio other = (Julio) otherObj;
        return Objects.equals(this.getName(), other.getName());
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.getName());
    }

    @Override
    public String toString() {
        return getClass().getName() + "[name=" + this.getName() + "]";
    }
}
