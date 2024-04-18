package Pokemons;

import Attacks.DracoMeteor;
import Attacks.ScaryFace;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Deino extends Pokemon {
    public Deino(String name, int level){
        super(name, level);
        setType(Type.DARK,Type.DRAGON);
        setStats(52,65,50,45,50,38);
        setMove(new DracoMeteor(),new ScaryFace());
    }
    public Deino(){
        super();
    }
}
