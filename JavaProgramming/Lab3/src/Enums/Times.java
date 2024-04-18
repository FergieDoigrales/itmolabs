package Enums;

public enum Times {
    AtThisTime("в это время"),
    Suddenly("Неожиданно"),
    AtThisTime2("Тем временем");
    public String label;

    private Times(String label) {
        this.label = label;
    }
}
