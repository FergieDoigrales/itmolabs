<%@ page import="com.mashaweblab2.model.Entries" %>
<%@ page import="com.mashaweblab2.model.Entry" %>

<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<% Entries entries = ((Entries) request.getServletContext().getAttribute("entries"));
    if (entries != null) {
        for (Entry entry : entries.getEntries()) {%>
<circle id="point"
        r="4"
        cx="<%=((300 / 2 + (entry.getX() + 0.02) / entry.getR() * 100))%>"
        cy="<%=((300 / 2 + (entry.getY() - 0.02) / entry.getR() * -100))%>"
        fill="<%=entry.isResult() ? "green" : "red"%>"
        stroke="white" />
<%}}%>
