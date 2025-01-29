<?php
class Youn_Movies_Model_Celebrity extends Mage_Core_Model_Abstract
{
    public function __construct()
    {
        $this->_init('youn_movies/celebrity');
        parent::_construct();
    }
}
