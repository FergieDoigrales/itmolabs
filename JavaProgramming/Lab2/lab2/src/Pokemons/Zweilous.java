package Pokemons;

import Attacks.DoubleHit;
import ru.ifmo.se.pokemon.Type;

public class Zweilous extends Deino {
    public Zweilous(String name, int level){
        super(name, level);
        addMove(new DoubleHit());
        setStats(72,85,70,65,70,58);
    }
    public Zweilous(){
        super();
    }

}
