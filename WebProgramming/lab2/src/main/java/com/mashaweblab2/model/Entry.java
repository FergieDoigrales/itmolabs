package com.mashaweblab2.model;

import java.util.Date;

public class Entry {
    private double x;
    private double y;
    private double r;
    private boolean result;
    private Date time;

    public Entry(double x, double y, double r, boolean result, Date time) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.result = result;
        this.time = time;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getR() {
        return r;
    }

    public boolean isResult() {
        return result;
    }

    public Date getTime() {
        return time;
    }
}
