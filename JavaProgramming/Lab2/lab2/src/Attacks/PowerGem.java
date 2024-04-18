package Attacks;

import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class PowerGem extends SpecialMove {
    public PowerGem(){
        super(Type.ROCK, 80, 100);
    }
    public String describe(){
        int B = 10;
        int type_of_describe =  (int) (Math.random() * B) + 3;
        if (type_of_describe <= 9) {
            return "почти устроил мортал комбат Х" /*+ String.valueOf(type_of_describe)*/;
        }
        return "дал по морде оппоненту" /*+ String.valueOf(type_of_describe)*/;

    }

}
