package Exceptions;

public class DoorIsClosedException extends RuntimeException {  //непроверяемое исключение
    @Override
    public String toString() {
        return "Дверь закрыта на ключ.";
    }
}
