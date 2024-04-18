<?php
session_start();
if (!isset($_SESSION['table'])) {
   $_SESSION['table'] = [];
}
foreach ($_SESSION['table'] as $string) {
    $string_color = null;
    if ($string['hit'] === 'Попал') $string_color = 'table-response-right';
    else $string_color = 'table-response-wrong';

    echo '<tr class="'.$string_color.'">
                        <th>'.$string['x'].'</th>
                        <th>'.$string['y'].'</th>
                        <th>'.$string['r'].'</th>
                        <th>'.$string['time'].'</th>
                        <th>'.$string['execution_time']. ' мс</th>
                        <th>'.$string['hit'].'</th>
                    </tr>';
} 