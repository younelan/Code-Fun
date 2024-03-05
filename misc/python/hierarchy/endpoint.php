<?php
$employees = json_decode(file_get_contents('employees.json'),true);
$base_uri="/linkedin/endpoint.php/";
$request = str_ireplace($base_uri,'',rawurldecode($_SERVER['REQUEST_URI']));
$cur_path = str_ireplace($_SERVER['PHP_SELF'], '', $request);
$pieces=explode('/',$cur_path);

if($pieces) {
  ( isset($pieces[0] )  ) ? $action=$pieces[0]:$action='';
  ( isset($pieces[1] )  ) ? $id=$pieces[1]:$id='';
}else {
  $action="";
  $id="";
}
if(! $action  ) {
  print json_encode($employees);
}
elseif( $id ) {
 print(json_encode($employees[$id] ) );
} else {
  exit('{"error":"Need employee id"}');
}
