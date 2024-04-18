package Peoples;

import Enums.Locations;

import java.util.Objects;

public class FixFex extends Person{

    public FixFex(String name) {
        super(name);
    }
    public String fell(Locations place){
        return this.getName() + " тоже свалились " + place.label + ".";
    }
    @Override
    public boolean equals(Object otherObj) {
        if (this == otherObj) return true;
        if (otherObj == null) return false;
        if (!this.getClass().equals(otherObj.getClass())) return false;
        FixFex other = (FixFex) otherObj;
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
