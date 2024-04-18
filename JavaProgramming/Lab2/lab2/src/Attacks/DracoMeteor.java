package Attacks;

import ru.ifmo.se.pokemon.*;

public class DracoMeteor extends SpecialMove {
    public DracoMeteor(){
        super(Type.DRAGON, 130,90);
    }
    public String describe(){
        return "неплохо так откостылял оппонента";
    }
    public void applyOppEffects(Pokemon p){
        p.addEffect(new Effect().stat(Stat.SPECIAL_ATTACK, -2));
    }

}
