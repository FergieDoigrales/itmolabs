import Enums.Adverbs;
import Enums.Locations;
import Enums.Times;
import Exceptions.DoorIsClosedException;
import Items.Door;
import Items.Item;
import Peoples.*;

public class Story {
    public static void storyTell() {
        Julio julio = new Julio("");
        System.out.print(julio.gagMouth(Times.Straightaway));
        Fix fix = new Fix("Фикс");
        System.out.print(fix.go(Adverbs.dutifully));
        MrClops mrClops = new MrClops("Господин Клопс");
        Fex fex = new Fex("Фекс");
        System.out.println(fex.appear(Times.AtThisTime, Locations.fromHome));
        Item gag = new Item("резиновый кляп");
        System.out.println(fex.gagedMouth(gag));
        System.out.print(mrClops.sit(Locations.home, Times.AtThisTime) + " ");
        Item cocoa = new Item("какао");
        Item cupOfCocoa = new Item("большой голубой кружки");
        System.out.println(mrClops.drink(cocoa, cupOfCocoa));

        Door door = new Door("дверь");
        try {
            System.out.print(door.open(Times.Suddenly)); //проверка на возможность открыть дверь.
        } catch (DoorIsClosedException e) {
            System.out.print(e);
            System.out.println(" У полицейских не вышло открыть замок.");
            return;
        }
        System.out.println(mrClops.see());
        cupOfCocoa.setName("большую голубую кружку");
        System.out.println(mrClops.spoiledCocoa(cupOfCocoa, cocoa));
        mrClops.setName("Клопс");
        Item chair = new Item("стул");
        Miga miga = new Miga("Мига");
        System.out.println(miga.whileTalking(julio.tieSomeOne(mrClops, chair)));
        Item truncheon = new Item("электрической дубинкой");
        System.out.println(julio.saw(mrClops.tryingStand(), truncheon));
        System.out.println(mrClops.fall(chair));
        System.out.print(miga.setTogether(Times.AtThisTime2));
        System.out.println(miga.makeToDo(truncheon));

        SomethingDoing kozlik = new SomethingDoing() { //анонимный вложенный класс через интерфейс
            @Override
            public void toDoSomething() {
                System.out.println("Козлик, оставшись в комнате, внимательно следил за лежавшим " + mrClops.getName() + "ом, "
                        + fix.getName() + "ом и " + fex.getName() + "ом.");
            }
        };

        var kozlikNew = new Person(" "){ //анонимный вложенный класс

            public void pokeWithATruncheon(String clops, String fix, String fex, String spaceSuit) {
                System.out.print("Если кто-нибудь зашевелится - козлик ткнет его дубинкой. ");
                String phrase = " - Козлик и ткнул его концом электрической дубинки в затылок, приговаривая: \"";
                if (clops.equals("Господин Клопс пошевелился, "))
                    System.out.println(clops + phrase + "\n" + spaceSuit + "\".");
                else if (fix.equals("Фикс пошевелился, "))
                    System.out.println(fix + phrase + "\n" + spaceSuit + "\".");
                else if (fex.equals("Фекс пошевелился, "))
                    System.out.println(fex + phrase + "\n" + spaceSuit + "\".");
            }
        };
        Item.SpaceSuit spaceSuit = new Item.SpaceSuit();
        System.out.println(julio.goOut(miga, Locations.yard, spaceSuit));
        kozlik.toDoSomething();
        Neznaika neznaika = new Neznaika("Незнайка");
        kozlikNew.pokeWithATruncheon(mrClops.move(), fix.move(), fex.move(), neznaika.leaveTheSpaceSuit(spaceSuit));
        System.out.println(miga.makeSomeoneToDo(julio, spaceSuit));
    }
}
