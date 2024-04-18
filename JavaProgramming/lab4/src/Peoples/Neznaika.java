package Peoples;


public class Neznaika extends Person {

    public Neznaika(String name) {
        super(name);
    }

    public String leaveTheSpaceSuit(Items.Item.SpaceSuit spaceSuit) {
        return "после получасовых поисков " + spaceSuit.getName() + " был найден на том же месте, где его оставил " + this.getName();
    }
}
