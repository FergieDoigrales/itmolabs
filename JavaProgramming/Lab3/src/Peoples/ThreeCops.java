package Peoples;

import Enums.Locations;

import java.util.Objects;

public class ThreeCops extends Person{
    public ThreeCops(String name) {
        super(name);
    }
    public String enter(Locations location, FixFex fixAndFex){
        return this.getName() + " ввалились в " + location.label + ", а вместе с ними " + fixAndFex.getName()
                + " со связанными руками и заткнутыми ртами. ";
    }
    @Override
    public boolean equals(Object otherObj) {
        if (this == otherObj) return true;
        if (otherObj == null) return false;
        if (!this.getClass().equals(otherObj.getClass())) return false;
        ThreeCops other = (ThreeCops) otherObj;
        return Objects.equals(this.getName(), other.getName());
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.getName());
    }

    @Override
    public String toString() {
        return getClass().getName() + "[name=" + this.getName() + "]";
    }
}
