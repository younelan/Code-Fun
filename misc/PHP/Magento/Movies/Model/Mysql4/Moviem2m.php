<?php
class Youn_Movies_Model_Mysql4_Moviem2m extends Mage_Core_Model_Mysql4_Abstract
{
    public function _construct()
    {
        $this->_init('youn_movies/moviem2m', 'm2m_id');
    }
}
