package Pokemons;

import Attacks.Flamethrower;
import Attacks.Overheat;
import Attacks.PowerGem;
import Attacks.Thunder;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Dialga extends Pokemon {
    public Dialga(String name, int level){
        super(name,level);
        setType(Type.STEEL,Type.DRAGON);
        setStats(100,120,120,150,100,90);
        setMove(new PowerGem(), new Overheat(), new Flamethrower(), new Thunder());
    }
    /*public String describe(){
        return "устроил мортал комбат Х";
    }*/

}
