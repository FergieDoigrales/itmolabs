package Attacks;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class ZenHeadbutt extends PhysicalMove {
    public ZenHeadbutt(){
        super(Type.PSYCHIC, 80, 90);
    }
    public String describe(){
        return "поиграл в кошки-мышки с оппонетом";
    }
    public void applyOppEffects(Pokemon p){
        if (new Effect().chance(0.2).success())
            Effect.flinch(p);
    }


}
