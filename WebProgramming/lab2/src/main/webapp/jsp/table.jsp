<%@ page import="com.mashaweblab2.model.Entries" %>
<%@ page import="com.mashaweblab2.model.Entry" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<div class="results"> <!--Блок для результатов-->
    <table id="result-table">
        <thead>
        <tr class="table-header">
            <th scope="col">X</th>
            <th scope="col">Y</th>
            <th scope="col">R</th>
            <th scope="col">Текущее время</th>
            <th scope="col">Результат</th>
        </tr>
        </thead>
        <tbody>
        <!--сюда вставляется результат-->
        <%  Entries entries = ((Entries) request.getServletContext().getAttribute("entries"));
            if (entries != null) {
                for (Entry entry : entries.getEntries()) {%>
        <tr class="<%=entry.isResult() ? "table-response-right" : "table-response-wrong"%>">
            <th><%=entry.getX()%></th>
            <th><%=entry.getY()%></th>
            <th><%=entry.getR()%></th>
            <th><%=entries.getSimpleDateFormat().format(entry.getTime())%></th>
            <th><%=entry.isResult() ? "Попал" : "Мимо"%></th>
        </tr>
        <%}}%>

        </tbody>
    </table>
</div> <!--Блок для результатов-->
