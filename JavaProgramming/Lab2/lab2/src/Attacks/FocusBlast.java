package Attacks;

import ru.ifmo.se.pokemon.*;

public class FocusBlast extends SpecialMove {
    public FocusBlast(){
        super(Type.FIGHTING, 120, 70);
    }
    public String describe(){
        return "намял бока оппоненту, используя скилл FocusBlast";
    }
    public void applyOppEffects(Pokemon p){
        p.addEffect(new Effect().chance(0.2).stat(Stat.DEFENSE, -1));
    }
}
