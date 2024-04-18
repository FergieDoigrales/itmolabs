import Pokemons.*;
import ru.ifmo.se.pokemon.Battle;
import ru.ifmo.se.pokemon.Pokemon;
public class Main {
    public static void main (String[] args){
        /*Battle b = new Battle();
        Pokemon p1 = new Pokemon("Чужой", 1);
        Pokemon p2 = new Pokemon("Хищник", 1);
        b.addAlly(p1);
        b.addFoe(p2);
        b.go();*/
        Battle b = new Battle();
      Pokemon dialga = new Dialga("Санчоус",1);
      Pokemon slowpoke = new Slowpoke("Никита Рыскаль", 20);
      Pokemon deino = new Deino("Кент", 13);
      Pokemon slowbro = new Slowbro("Чент", 100);
      Pokemon zweilous = new Zweilous("Слонсер", 60);
      Pokemon hydreigon = new Hydreigon("Илюха", 60);
      b.addAlly(dialga);
      b.addAlly(deino);
      b.addAlly(hydreigon);
      b.addFoe(slowpoke);
      b.addFoe(slowbro);
      b.addFoe(zweilous);
      b.go();
      System.out.println("Не хватает пива и чипсов..");

    }
}
