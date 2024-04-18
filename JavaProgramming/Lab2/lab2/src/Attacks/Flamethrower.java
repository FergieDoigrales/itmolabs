package Attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Flamethrower extends SpecialMove {
    public Flamethrower(){
        super(Type.FIRE, 90, 100);
    } public String describe() {
        return "закастовал Flamethrower" /*+ String.valueOf(type_of_describe)*/;
    } public void applyOppEffects(Pokemon p){
        if (new Effect().chance(0.3).success())
            Effect.burn(p);

    }
}
