package Attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Thunder extends SpecialMove {
    public Thunder(){
        super(Type.ELECTRIC, 110, 70);
    } public String describe() {
        return "бонкнул оппонента";
    } public void applyOppEffects(Pokemon p){
        if (new Effect().chance(0.3).success())
            Effect.paralyze(p);
    }
}
