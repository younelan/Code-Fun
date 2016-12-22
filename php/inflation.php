<?php
 /* simple scrip to scrape inflation rates located at */
        $url='http://www.usinflationcalculator.com/inflation/historical-inflation-rates/';
/* + sort rowx by average inflation */
/* + generate sql statements to insert rows */
        //set showTable to false to show the sql insert statements
        $showTable=true;
        //minimum table column width
        $colWidth=5;

        //detect if we are in a browser and add a <pre>
        if (php_sapi_name() != "cli") {
            print '<pre>';
        }

        $page=file_get_contents($url);
        //remove the footer
        list($page,$footer)=explode('</table>',$page);
        //split into rows
        $rows=preg_split('/<tr.*>/',$page);
        //remove the header
        unset($rows[0]);
        //get column names
        $columns=$values=preg_split('/\s+/', strip_tags($rows[1]));
        //remove blank values
        unset($columns[0]);
        unset($columns[15]);
        unset($rows[1]);
        //make column names lowercase (sample is like that)
        $columns = array_map('strtolower' , $columns);
        foreach($rows as $row) {
                $values=preg_split('/\s+/', strip_tags($row));
                //remove blank values
                unset($values[0]);
                unset($values[15]);
                $values=str_replace('&nbsp;','',$values);
                //turn it into an associative array
                $resultSet[(float) $values[1]]=(array_combine($columns,$values));
                //ready to be sorted
                $sort_array[(float)$values[1]]=$values[14];
        }
        //sort results
        array_multisort($sort_array,SORT_DESC,$resultSet);


        if($showTable) {

                //print table header
                print str_repeat('-', count($columns)*($colWidth+1)+1) . "\n";

                foreach($columns as $val) {
                        print "|" . str_pad($val, $colWidth, ' ', STR_PAD_LEFT);
                }
                print "|\n";
                print str_repeat('-', count($columns)*($colWidth+1)+1) . "\n";
                //print results
                foreach($resultSet as $row) {
                        foreach($row as $val) {
                                print "|" . str_pad($val, $colWidth, ' ', STR_PAD_LEFT);
                        }
                        print "|\n";
                }
                print str_repeat('-', count($columns)*($colWidth+1)+1) . "\n";

        }else { //show query
                foreach($columns as $val) {
                        $fields[]="    `$val` DOUBLE";
                }
                print "DROP TABLE IF EXISTS statistics;\nCREATE TABLE statistics\n(\n    ";
                print implode(",\n    ", $fields);
                print "\n);\n";
                foreach($resultSet as $row) {
                        print "INSERT INTO statistics (`" .
                                     implode("`,`" , $columns) .
                                  "`) \n      VALUES ('" .
                                     implode("','" , $row) .
                                  "');\n";
                }
        }


