<?php
class Youn_Movies_Model_Movie extends Mage_Core_Model_Abstract
{
    public function __construct()
    {
        $this->_init('youn_movies/movie');
        parent::_construct();
    }
/* kept this method from gift registry as it shows orm
    public function updateMovieData(Mage_Customer_Model_Customer $customer, $data)
    {
        try{
            if(!empty($data))
            {
                $this->setCustomerId($customer->getId());
                $this->setWebsiteId($customer->getWebsiteId());
                $this->setTypeId($data['type_id']);
                $this->setEventName($data['event_name']);
                $this->setEventDate($data['event_date']);
                $this->setEventCountry($data['event_country']);
                $this->setEventLocation($data['event_location']);
            }else{
                throw new Exception("Error Processing Request: Insufficient Data Provided");
            }
        } catch (Exception $e){
            Mage::logException($e);
        }
        return $this;
    }
*/
}
