package Attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class ThunderWave extends StatusMove {
    public ThunderWave(){
        super(Type.ELECTRIC, 0,90);
    }public String describe() {
        return "бонкнул оппонента";
    }public void applyOppEffects(Pokemon p){
        Effect.paralyze(p);
    }


}
