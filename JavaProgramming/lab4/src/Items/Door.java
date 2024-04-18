package Items;

import Enums.Times;
import Exceptions.DoorIsClosedException;

public class Door extends Item {
    boolean isClosed = false;

    public Door(String name) {
        super(name);
    }

    public String open(Times time) {
        int opposity = (int) (Math.random() * 6);
        if (opposity > 3) {
            isClosed = true;
            throw new DoorIsClosedException(); //дверь может быть закрыта, в таком случае история прерывается
        }
        return time.label + " " + getName() + " отворилась, ";
    }
}
