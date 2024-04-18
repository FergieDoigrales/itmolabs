package Enums;

public enum Locations {
    home("дома"),
    fromHome("из дома"),
    room("комнату"),
    floor("на пол"),
    yard("во двор");
    public String label;

    Locations(String label) {

        this.label = label;
    }

}
