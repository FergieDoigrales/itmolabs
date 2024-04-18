package Peoples;

import Enums.Times;
import Items.Item;

import java.util.Objects;

public class Miga extends Person{
    public Miga(String name) {
        super(name);
    }
    public String whileTalking(String whatHappened){
        return "Пока " + this.getName() + " говорил, " + whatHappened + " ";
    }
    public String setTogether(Times time, Person person){
        return time.label + " " + this.getName() + " поставил " + person.getName() + " рядышком. ";
    }
    public String makeToDo(Item item, String whatHappened){
        return "Приказав им стоять смирно, " + this.getName() + " треснул каждого по лбу " + item.getName() + ", отчего " + whatHappened;
    }
    @Override
    public boolean equals(Object otherObj) {
        if (this == otherObj) return true;
        if (otherObj == null) return false;
        if (!this.getClass().equals(otherObj.getClass())) return false;
        Miga other = (Miga) otherObj;
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
