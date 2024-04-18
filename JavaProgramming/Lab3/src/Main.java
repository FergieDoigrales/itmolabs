import Enums.Locations;
import Enums.Times;
import Items.Door;
import Items.Item;
import Peoples.*;

import java.net.SocketTimeoutException;

public class Main {
    public static void main(String[] args) {
        MrClops mrClops = new MrClops("Господин Клопс");
        System.out.print(mrClops.sit(Locations.HOME, Times.AtThisTime) + " ");
        Item cocoa = new Item("какао");
        Item cupOfCocoa = new Item("большая голубая кружка");
        System.out.println(mrClops.drink(cocoa, cupOfCocoa));
        Door door = new Door("дверь");
        System.out.print(door.open(Times.Suddenly));
        ThreeCops cops = new ThreeCops("трое полицейских");
        FixFex fixFex = new FixFex("Фикс и Фекс");
        System.out.println(mrClops.see(cops.enter(Locations.ROOM, fixFex)));
        System.out.println(mrClops.spoiledCocoa(cupOfCocoa, cocoa));
        Item chair = new Item("стул");
        Miga miga = new Miga("Мига");
        Julio julio = new Julio("Жулио");
        System.out.println(miga.whileTalking(julio.tieSomeOne(mrClops, chair)));
        Item truncheon = new Item("электрической дубинкой");
        System.out.println(julio.saw(mrClops.tryingStand(),truncheon));
        System.out.println(mrClops.fall(chair));
        System.out.print(miga.setTogether(Times.AtThisTime2, fixFex));
        System.out.println(miga.makeToDo(truncheon, fixFex.fell(Locations.FLOOR)));
    }
}