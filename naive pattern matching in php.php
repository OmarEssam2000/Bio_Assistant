<?php
        function SearchString($str, $pat)
        {
            $retVal = array();
            $M = strlen($pat);
            $N = strlen($str);
        
            for ($i = 0; $i <= $N - $M; $i++)
            {
                $j = 0;
        
                for ($j = 0; $j < $M; $j++)
                {
                    if ($str[$i + $j] != $pat[$j])
                        break;
                }
        
                if ($j == $M)
                    array_push($retVal, $i);
            }
        
            return $retVal;
        }
        $data = "the quick brown fox jumps over the lazy dog";
        $value = SearchString($data, "the");
         ?>