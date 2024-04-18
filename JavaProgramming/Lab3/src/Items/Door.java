package Items;

import Enums.Times;

public class Door extends Item{
    public Door(String name) {
        super(name);
    }
    public String open(Times time){
        return time.label + " " + getName() + " отворилась, ";
    }
}
