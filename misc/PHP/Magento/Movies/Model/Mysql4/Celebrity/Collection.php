<?php
class Youn_Movies_Model_Mysql4_Celebrity_Collection extends Mage_Core_Model_Mysql4_Collection_Abstract
{
    public function _construct()
    {
        $this->_init('youn_movies/celebrity');
        parent::_construct();
    }
}
