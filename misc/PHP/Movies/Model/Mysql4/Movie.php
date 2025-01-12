<?php
class Youn_Movies_Model_Mysql4_Movie extends Mage_Core_Model_Mysql4_Abstract
{
    public function _construct()
    {
        $this->_init('youn_movies/movie', 'movie_id');
    }
}
