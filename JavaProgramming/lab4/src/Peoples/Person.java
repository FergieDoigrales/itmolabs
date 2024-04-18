package Peoples;

import Exceptions.MissingNameException;

import java.util.Objects;

public abstract class Person {
    private String name;

    public Person(String name) {
        try {
            if (name.equals(""))
                throw new MissingNameException();
            this.name = name;
            //joinStory();
        } catch (MissingNameException e) {
            System.out.println(e);
            System.out.println("ЗАДАЙТЕ ИМЯ ДЛЯ ОБЪЕКТА ТИПА " + this.getClass());
            this.name = "NO_NAME";
        }
    }
    protected void joinStory(){
        System.out.print("(" + "в истории появляется " +  this.getName() + ") ");
    }


    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean equals(Object otherObj) {
        if (this == otherObj) return true;
        if (otherObj == null) return false;
        if (!this.getClass().equals(otherObj.getClass())) return false;
        Person other = (Person) otherObj;
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
