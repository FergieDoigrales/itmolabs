package Attacks;

import ru.ifmo.se.pokemon.*;

public class ScaryFace extends StatusMove {
    public ScaryFace(){
        super(Type.NORMAL, 0, 100);
    }
    public String describe(){
        return "отчихвостил оппонента";
    }
    public void applyOppEffects(Pokemon p){
        p.addEffect(new Effect().stat(Stat.SPEED, -2));
    }
}
