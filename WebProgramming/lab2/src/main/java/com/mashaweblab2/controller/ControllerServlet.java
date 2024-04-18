package com.mashaweblab2.controller;

import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/controller")
public class ControllerServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        try {
            ServletContext context = getServletContext();
            String action = req.getParameter("action");
            if (action.equals("clear")) {
                context.setAttribute("entries", null);
                return;
            }
            double x = Double.parseDouble(req.getParameter("x").replace(",", "."));
            double y = Double.parseDouble(req.getParameter("y").replace(",", "."));
            double r = Double.parseDouble(req.getParameter("r").replace(",", "."));
            if (!(r >= 2.0 && r <= 5.0)) {
                throw new Exception("Радиус задан некорректно");
            }
            req.setAttribute("xValue", x);
            req.setAttribute("yValue", y);
            req.setAttribute("rValue", r);
            context.getRequestDispatcher("/area_check").forward(req, resp);

        } catch (Exception e) {
            resp.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
    }
}
