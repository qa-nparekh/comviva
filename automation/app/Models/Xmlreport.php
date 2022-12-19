<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use DB;
use Session;
use Route;
use App\Models\Usersreport;

class Xmlreport extends Model
{
    use HasFactory;
    protected $table = 'result_reports';


    public function save_upload_xml_report($requestData){
        $data = Auth()->guard('admin')->user();
        
        $image = $requestData['xml_files'];
        $xml_files_name = 'xml_files.'.$image->getClientOriginalExtension();
        $destinationPath = public_path('/backend_automation/'.str_replace(' ', '_', $data['first_name'])."_".str_replace(' ', '_', $data['last_name'])."_".$data['user_no']);
        if($image->move($destinationPath, $xml_files_name)){

            $xmlString = file_get_contents(public_path('/backend_automation/'.str_replace(' ', '_', $data['first_name'])."_".str_replace(' ', '_', $data['last_name'])."_".$data['user_no']).'/xml_files.xml');

            $xmlObject = simplexml_load_string($xmlString);

            $json = json_encode($xmlObject);
            $dataArray = json_decode($json, true);

            $resultArr = [];
            foreach($dataArray['event'] as $key => $value){


                $count =  Resultreport::where('result_reports.event_time', date("Y-m-d H:i:s", strtotime($value['@attributes']['eventTimestamp'])))
                                ->where('result_reports.brand', $value['sender']['@attributes']['from'])
                                ->where('result_reports.sender_address', $value['sender']['@attributes']['msisdn'])
                                ->where('result_reports.recipient_msisdn', $value['recipients']['recipient']['@attributes']['code'])
                                ->where('result_reports.sccp_gt', $value['sender']['@attributes']['sccpAddress'])
                                ->where('result_reports.status', $value['result']['@attributes']['value'])
                                ->count();

                if($count == 0){
                    $resultArr[] = [
                        'event_time' => date("Y-m-d H:i:s", strtotime($value['@attributes']['eventTimestamp'])),
                        'brand' => $value['sender']['@attributes']['from'],
                        'sender_address' => $value['sender']['@attributes']['msisdn'],
                        'recipient_msisdn' => $value['recipients']['recipient']['@attributes']['code'],
                        'sccp_gt' => $value['sender']['@attributes']['sccpAddress'],
                        'status' => $value['result']['@attributes']['value'],
                        'received_content' => $value['payload']['message']['textBody'],
                        'created_at' => date('Y-m-d H:i:s'),
                        'updated_at' => date('Y-m-d H:i:s'),
                    ];
                }
            }

            if(Resultreport::insert($resultArr)){
                $currentRoute = Route::current()->getName();
                $inputData = $resultArr;
                unset($inputData['_token']);
                $objAudittrails = new Audittrails();
                $res = $objAudittrails->add_audit('Insert','admin/'. $currentRoute , json_encode($inputData) ,'Brand Entry' );
                return 'true';
            }else{
                return 'false';
            }
            
            return true;

        }
        return false;
    }
}
