package Attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class FireBlast extends SpecialMove {
    public FireBlast(){
        super(Type.FIRE, 110, 85);
    }
    public String describe(){
        return "заставил своего соперника глотать пыль";
    }
    public void applyOppEffects(Pokemon p){
        if (new Effect().chance(0.1).success())
            Effect.burn(p);

    }
}
