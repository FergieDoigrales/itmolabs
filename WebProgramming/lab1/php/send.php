<?php
function validate_num($num, $a, $b) {
    return isset($num) && is_numeric($num) && $num >= $a && $num <= $b;
}

function check_rectangle($x, $y, $r) { //проверка попадания в прямоугольник
    return $x>=0 && $y <= 0 && $x <= $r && $y >= -$r;
}

function check_triangle($x, $y, $r) { // треугольник
    return $x>=0 && $y>=0 && $x<=$r && $y<=$r && $x*$y <= $r*$r;
}

function check_circle($x, $y, $r) { // четверть круга
    return $x<=0 && $y>=0 && sqrt($x*$x+$y*$y)<=abs($r)/2;
}

session_start();
if (!isset($_SESSION['table'])) {
    $_SESSION['table'] = [];
}
$start = microtime(true);
date_default_timezone_set('Europe/Moscow');


$x = @$_GET['x'];
$y = @$_GET['y'];
$r = @$_GET['r'];

// добавить время

if (validate_num($x, -2, 2) && validate_num($y, -3, 5) && validate_num($r, 1, 3)) {
    $hit = check_rectangle($x, $y, $r) || check_triangle($x, $y, $r) || check_circle($x, $y, $r) ? 'Попал' : 'Мимо';
    $time = date('H:i:s');
    $execution_time = number_format(microtime(true) - $start, 10, '.', '')*1000000;
    $execution_time = number_format($execution_time, 2);
    array_push($_SESSION['table'], ['x'=>$x, 'y'=>$y, 'r'=>$r, 'time'=>$time, 'execution_time'=> $execution_time, 'hit'=>$hit]);
}

foreach($_SESSION['table'] as $string) {
    $string_color = null;
    if ($string['hit'] === 'Попал') $string_color = 'table-response-right';
    else $string_color = 'table-response-wrong';

    echo '<tr class="'.$string_color.'">
                        <th>'. $string['x'] .'</th>
                        <th>'. $string['y'] .'</th>
                        <th>'. $string['r'] .'</th>
                        <th>'.$string['time'].'</th>
                        <th>'.$string['execution_time']. ' мс</th>
                        <th>'. @$string['hit'] .'</th>
                        </tr>';
}