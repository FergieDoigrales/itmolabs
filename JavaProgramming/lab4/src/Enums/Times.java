package Enums;

public enum Times {
    AtThisTime("в это время"),
    Suddenly("Неожиданно"),
    AtThisTime2("Тем временем"),

    Straightaway("тут же");
    public String label;

    Times(String label) {
        this.label = label;
    }
}
