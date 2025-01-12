<?php
class Youn_Movies_Helper_Data extends Mage_Core_Helper_Abstract {
    public function getMovies()
    {
        $collection = Mage::getModel('youn_movies/movie')->getCollection();
        return $collection;
    }
    /*kept this function from gift registry for now
    public function isRegistryOwner($registryCustomerId)
    {
        $currentCustomer = Mage::getSingleton('customer/session')->getCustomer();
        if($currentCustomer && $currentCustomer->getId() == $registryCustomerId)
        {
            return true;
        }
        return false;
    }*/

}

