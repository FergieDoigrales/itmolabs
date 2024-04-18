package Attacks;

import ru.ifmo.se.pokemon.*;

public class SteelWing extends PhysicalMove {
    public SteelWing(){
        super(Type.STEEL,70,90);
    }
    public String describe(){
        return "попытался переспорить оппонента, но не справился с гневом";
    }
    public void applySelfEffects(Pokemon p){
        p.addEffect(new Effect().chance(0.1).stat(Stat.DEFENSE, +1));
    }
}
