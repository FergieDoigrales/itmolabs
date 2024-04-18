package Attacks;
import ru.ifmo.se.pokemon.*;

public class Overheat extends SpecialMove {
    public Overheat(){
        super(Type.FIRE, 130, 90);
    }
    public String describe(){
        int B = 10;
        int type_of_describe =  (int) (Math.random() * B) + 3;
        if (type_of_describe <= 9) {
            return "легонько дал пенделя оппоненту";
        }
        return "дал леща сопернику";
    }
    public void applySelfEffects(Pokemon p){
        p.addEffect(new Effect().stat(Stat.SPECIAL_ATTACK, -2));
    }

}
