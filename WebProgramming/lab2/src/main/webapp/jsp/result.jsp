<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab №1</title>
    <link rel="stylesheet" href="<%= request.getContextPath()%>/css/style.css">
    <link rel="stylesheet" href="<%= request.getContextPath()%>/css/form.css">
    <link rel="stylesheet" href="<%= request.getContextPath()%>/css/table.css">
</head>
<body>
<div class="pink">
    <span id="main-text">P3218 LW2 #11323 Bogdanova Maria Mikhailovna</span>
    <div class="grap-form">

        <div class="graph"> <!--Блок для графика-->
            <svg height="300" width="300" xmlns="http://www.w3.org/2000/svg">
                <!-- Первая фигура - треугольник -->
                <polygon fill="#f8e0e0"
                         fill-opacity="1"
                         stroke="#f8e0e0"
                         points="100,150 150,150 150,250"></polygon>

                <!-- Вторая фигура - квадрат -->
                <polygon fill="#f8e0e0"
                         fill-opacity="1"
                         stroke="#f8e0e0"
                         points="250,150 150,150 150,100 250,100"></polygon>

                <!-- Третья фигура - четверть круга -->
                <path fill="#f8e0e0"
                      fill-opacity="1"
                      stroke="#f8e0e0"
                      d="M 200 150 C 200 200, 150 200, 150 200 L 150 150 Z"></path>

                <!-- Стрелки и оси -->
                <line stroke="black" x1="0" x2="300" y1="150" y2="150"></line>
                <line stroke="black" x1="150" x2="150" y1="0" y2="300"></line>
                <polygon fill="black" points="150,0 144,15 156,15" stroke="black"></polygon>
                <polygon fill="black" points="300,150 285,156 285,144" stroke="black"></polygon>

                <!-- Деления -->
                <line stroke="black" x1="200" x2="200" y1="155" y2="145"></line>
                <line stroke="black" x1="250" x2="250" y1="155" y2="145"></line>

                <line stroke="black" x1="50" x2="50" y1="155" y2="145"></line>
                <line stroke="black" x1="100" x2="100" y1="155" y2="145"></line>

                <line stroke="black" x1="145" x2="155" y1="100" y2="100"></line>
                <line stroke="black" x1="145" x2="155" y1="50" y2="50"></line>

                <line stroke="black" x1="145" x2="155" y1="200" y2="200"></line>
                <line stroke="black" x1="145" x2="155" y1="250" y2="250"></line>

                <!-- Подписи к делениям и осям -->
                <text fill="black" x="195" y="140">R/2</text>
                <text fill="black" x="250" y="140">R</text>

                <text fill="black" x="40" y="140">-R</text>
                <text fill="black" x="85" y="140">-R/2</text>

                <text fill="black" x="160" y="55">R</text>
                <text fill="black" x="160" y="105">R/2</text>

                <text fill="black" x="160" y="204">-R/2</text>
                <text fill="black" x="160" y="255">-R</text>

                <text fill="black" x="285" y="140">X</text>
                <text fill="black" x="160" y="15">Y</text>

                <circle r="3.5"
                        cx=<%=request.getServletContext().getAttribute("xGraph")%>
                                cy=<%=request.getServletContext().getAttribute("yGraph")%>
                        id="target-dot"
                        fill=<%=request.getServletContext().getAttribute("fillGraph")%>>
                </circle>

            </svg>
        </div>

        <div class="back">
            <a href="<%= request.getContextPath() %>/">Назад</a>
        </div>

        <div class="results"> <!--Блок для результатов-->
            <table id="result-table">
                <thead>
                <tr class="table-header">
                    <th scope="col">X</th>
                    <th scope="col">Y</th>
                    <th scope="col">R</th>
                    <th scope="col">Время</th>
                    <th scope="col">Результат</th>
                </tr>
                </thead>
                <tbody>
                    <tr class="<%=request.getServletContext().getAttribute("fillTable")%>">
                        <th><%=request.getServletContext().getAttribute("xLast")%></th>
                        <th><%=request.getServletContext().getAttribute("yLast")%></th>
                        <th><%=request.getServletContext().getAttribute("rLast")%></th>
                        <th><%=request.getServletContext().getAttribute("time")%></th>
                        <th><%=request.getServletContext().getAttribute("resultLast")%></th>
                    </tr>
                </tbody>
            </table>
        </div> <!--Блок для результатов-->
    </div>
</div> <!--Общий блок для картинки и формы -->

<script type="text/javascript" src="<%= request.getContextPath()%>/js/code.jquery.com_jquery-3.7.0.min.js"></script>
<script type="text/javascript" src="<%= request.getContextPath()%>/js/script.js"></script>
</body>
</html>