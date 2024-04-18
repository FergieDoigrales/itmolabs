package com.mashaweblab2.controller;

import com.google.gson.Gson;
import com.mashaweblab2.model.Entries;
import com.mashaweblab2.model.Entry;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@WebServlet("/area_check")
public class AreaCheckServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        double x = (double) req.getAttribute("xValue");
        double y = (double) req.getAttribute("yValue");
        double r = (double) req.getAttribute("rValue");
        String action = req.getParameter("action");


        if (r >= 2 && r <= 5) {
            boolean result = getResult(x, y, r);
            Date currentTime = new Date();

            Entry entry = new Entry(x, y, r, result, currentTime);


            ServletContext context = getServletContext();

            Entries entries =  (Entries) context.getAttribute("entries");
            entries = entries == null ? new Entries() : entries;

            entries.addEntry(entry);
            context.setAttribute("entries", entries);
            if (action.equals("form")) {
                setResult(x, y, r, result, currentTime, entries, req);
                req.getRequestDispatcher("./jsp/result.jsp").forward(req, resp);
            } else if (action.equals("grap")) {
                Gson gson = new Gson();
                Map<String, Object> json = new HashMap<>();
                json.put("x", x);
                json.put("y", y);
                json.put("r", r);
                json.put("result", result);
                json.put("time", entries.getSimpleDateFormat().format(currentTime));
                String responseMessage = gson.toJson(json);
                resp.getWriter().write(responseMessage);
            }

        }
    }

    private boolean getResult(double x, double y, double r) {
        return inTriangle(x, y, r) || inRectangle(x, y, r) || inCircle(x, y, r);
    }

    private boolean inTriangle(double x, double y, double r){
        return ((x <= 0) &&
                (y <= 0) &&
                (y >= -r) &&
                (x >= -r/2) &&
                (Math.abs(x)+Math.abs(y/2) <= r/2));
    }

    private boolean inRectangle(double x, double y, double r){
        return ((x >= 0) &&
                (y >= 0) &&
                (y <= r/2) &&
                (x <= r));
    }

    private boolean inCircle(double x, double y, double r){
        return ((x >= 0) &&
                (y <= 0) &&
                (x * x + y * y <= (r * r)/4));
    }

    private void setResult(double x, double y, double r, boolean result, Date currentTime, Entries entries, HttpServletRequest request){
        ServletContext context = getServletContext();
        context.setAttribute("xLast", x);
        context.setAttribute("yLast", y);
        context.setAttribute("rLast", r);
        context.setAttribute("time", entries.getSimpleDateFormat().format(currentTime));
        context.setAttribute("resultLast", result ? "Попал" : "Мимо");
        context.setAttribute("xGraph", (300 / 2 + (x + 0.02) / r * 100));
        context.setAttribute("yGraph", (300 / 2 + (y - 0.02) / r * -100));
        context.setAttribute("fillGraph", result ? "green" : "red");
        context.setAttribute("fillTable", result ? "table-response-right" : "table-response-wrong");
    }
}
