package Peoples;

import Enums.Locations;
import Enums.Times;
import Items.Item;

import java.util.Objects;

public class MrClops extends Person implements drinking{

    public MrClops(String name) {
        super(name);
    }
    public String sit(Locations location, Times time){
        return this.getName() + " сидел " + time.label + " " + location.label + ".";
    }
    public String drink(Item dinkr, Item container){
        return this.getName() + " попивал " + dinkr.getName() + " из " + container.getName() + ".";
    }
    public String see(String whatSee){
       return "и он увидел, как " + whatSee;
    }
    public String spoiledCocoa(Item item, Item item2){
        return this.getName() + " широко раскрыл рот и опрокинул " + item.getName() + " с горячим " + item2.getName() + " прямо себе на брюки. ";
    }
    public String tryingStand(){
        return this.getName() + " все же болтает ногами и пытается встать";
    }
    public String fall(Item item){
        return "В результате " + this.getName() + " полетел на пол вместе со " + item.getName() + "ом.";
    }
}
