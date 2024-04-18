package Enums;

public enum Locations {
    HOME("дома"),
    ROOM("комнату"),
    FLOOR("на пол");
    public String label;

    private Locations(String label) {

        this.label = label;
    }

}
