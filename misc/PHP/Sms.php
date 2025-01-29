<?php
/** Sms controller - provides a twilio endpoint */

namespace App\Controllers;

class Sms extends BaseController
{

	/** index function, provides an endpoint for twilio 
	 * parameters: none
	 * post variables:
	 *   from: number originating sms
	 *   body: content of sms
	 * output:
	 *   xml for twilio
	 */
	public function index()
	{
		$data['from']=$this->input->get_post('From');
		$body=$this->input->get_post('Body');
		if(strstr($body,' '))
		{
			$command=strtolower(substr($body,0,strpos($body,' ')));
			$param=substr($body,strpos($body,' ')+1);
		}
		else
		{
			$command=strtolower($body);
			$param='';
		}

		$data['reply']='Received from ' . $data['from'] . ': ' . $body;
		$data['reply']="command: '$command' <br/>param='$param'";
                try {
		$fp=@fopen(FCPATH . '/smslog.txt','a');
		@fwrite($fp,@date("d/m h:s ") . $data['from'] . ' ' . $body . "\n");
		@fclose($fp);
                }
                catch(Exception $e) {
                }
		switch($command)
		{
			case 'category':
				$query=$this->db
				->like('LOWER(catname)',strtolower($param))
				->get('node_tree');
				$category=0;
				$row=$query->result();
				//print_r($row);exit();
				if($row)
				{
					$category=$row[0]->treeid;
				}
				$this->load->model('Explorer_model');
				$links=$this->Explorer_model->getlinks($category,5,'random()');
				$names=null;
				foreach($links as $link) {
					$names[]=$link->title;
				}
				$data['reply']=implode("\n",$names);
				
				break;
			case 'zipcode':
			case 'zip':
				if(strlen($param)<2) {
					$data['reply']="Incorrect syntax. \n\nUsage:\nzip [zipcode]";
					break;
				}
				$where=array('nodes_details.field2'=>$param);
				$query=$this->db->select('*')->from('nodes')->join('nodes_details', 'nodes.id=nodes_details.nodeid')
                    ->order_by('title', 'random')
                    ->limit(5)->where($where)->get();

				$rows=$query->result();
				$places=null;
				foreach($rows as $row) {
					$places[]=$row->title;
				}
				if($places)
					$data['reply']= implode("\n" , $places);
				else
					$data['reply'] = 'No places in this zipcode';
				break;
                        case 'start':
			case 'info':
			case 'help':
				$data['reply']="Commands:\nplace [placename]\nzip [zipcode]\ncategory [category name]";
				break;
			case 'place':
			case 'poi':
				if(strlen($param)<2) {
					$data['reply']="Incorrect syntax. \n\nUsage:\nplace [placename]";
					break;
				}
                $query=$this->db->select('*')->from('nodes')->join('nodes_details', 'nodes.id=nodes_details.nodeid')
	                    ->order_by('title', 'random')
	                    ->like('LOWER(title)', strtolower($param))
	                    ->limit(5)->get();

				$row=$query->result();

				if($row)
				{
					if($row[0]->field1) $address[]=$row[0]->field1;
					if($row[0]->field2) $zipcode[]=$row[0]->field2;

					$data['reply']= $row[0]->title;
					if($row[0]->field4) $data['reply'] .="\nPhone: " . $row[0]->field4;
					if($row[0]->field1) $data['reply'] .= "\nAddress: " . $row[0]->field1;
					if($row[0]->field6) $data['reply'] .= "\nURL: " . $row[0]->field6;
					if($row[0]->field5) $data['reply'] .= "\n" . $row[0]->field5;
				}
				else
				{
					$data['reply']='Place not found. Please check spelling/Try a partial name. ';
				}
				break;
			default:
				$data['reply']="command $command not found";
		}
		$this->load->view('smsreply',$data);

	}
	function path() {
	}

}
