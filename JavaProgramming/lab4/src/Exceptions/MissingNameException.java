package Exceptions;

public class MissingNameException extends Exception { //проверяемое исключение
    @Override
    public String toString() {
        return "Отсутствует название/имя объекта (задана пустая строка).";
    }
}
