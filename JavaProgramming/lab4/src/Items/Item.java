package Items;

public class Item {
    private String name;

    public Item(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static class SpaceSuit {
        private static final String name = "скафандр";

        public String getName() {
            return name;
        }
    }
}
