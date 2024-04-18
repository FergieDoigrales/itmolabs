package Pokemons;

import Attacks.FireBlast;
import Attacks.ThunderWave;
import Attacks.ZenHeadbutt;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Slowpoke extends Pokemon {
    public Slowpoke(String name, int level){
        super(name,level);
        setType(Type.WATER,Type.PSYCHIC);
        setStats(90,65,65,40,40,15);
        setMove(new ThunderWave(), new ZenHeadbutt(),new FireBlast());
    }
    public Slowpoke(){
        super();
    }
}
