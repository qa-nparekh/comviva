<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use DB;
use Session;
use Route;
use App\Models\Usersreport;

class Resultreport extends Model
{
    use HasFactory;
    protected $table = 'result_reports';

    public function getdatatable($data_array)
    {
        $requestData = $_REQUEST;
        $columns = array(
            0 => 'result_reports.id',
            1 => 'result_reports.event_time',
            2 => 'mobile_number.operator',
            4 => 'result_reports.sender_address',
            5 => 'result_reports.sender_address',
            6 => 'result_reports.recipient_msisdn',
            7 => 'result_reports.sccp_gt',
            8 => 'result_reports.status',
            9 => 'result_reports.received_content',
        );

        $query = Resultreport ::from('result_reports')
                ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id')
                ->where('result_reports.uuid', null)
                ->where('result_reports.smsid', null);

        if($data_array['operator'] != 'all'){
            $query->where('mobile_number.operator', $data_array['operator']);
        }

        if($data_array['country_list'] != 'all'){
            $query->where("countries.id", $data_array['country_list']);
        }

        if($data_array['sender_from'] != 'all'){
            $query->where("result_reports.sender_address",$data_array['sender_from']);
        }

        if($data_array['from'] != '' || $data_array['from'] != null ){
            $from = date("Y-m-d",strtotime($data_array['from']));
            $query->whereDate('result_reports.event_time', '>=', $from);
        }

        if($data_array['to'] != '' || $data_array['to'] != null ){
            $to = date("Y-m-d",strtotime($data_array['to']));
            $query->whereDate('result_reports.event_time', '<=', $to);
        }

        if (!empty($requestData['search']['value'])) {   // if there is a search parameter, $requestData['search']['value'] contains search parameter
            $searchVal = $requestData['search']['value'];
            $query->where(function($query) use ($columns, $searchVal, $requestData) {
                $flag = 0;
                foreach ($columns as $key => $value) {
                    $searchVal = $requestData['search']['value'];
                    if ($requestData['columns'][$key]['searchable'] == 'true') {
                        if ($flag == 0) {
                            $query->where($value, 'like', '%' . $searchVal . '%');
                            $flag = $flag + 1;
                        } else {
                            $query->orWhere($value, 'like', '%' . $searchVal . '%');
                        }
                    }
                }
            });
        }

        $temp = $query->orderBy($columns[$requestData['order'][0]['column']], $requestData['order'][0]['dir']);

        $totalData = count($temp->get());
        $totalFiltered = count($temp->get());

        $resultArr = $query->skip($requestData['start'])
                    ->take($requestData['length'])
                    ->select('result_reports.id', 'brand_entry.brand_name',  'result_reports.event_time', 'mobile_number.mobile_number', 'mobile_number.operator', 'result_reports.brand', 'result_reports.sender_address', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'result_reports.status', 'result_reports.received_content')
                    ->get();



        $data = array();
        $i = 0;

        foreach ($resultArr as $row) {
            $received_content = strtoupper($row['received_content']);
            $senders_address = strtoupper($row['sender_address']);

            if (str_contains($received_content, $senders_address)) {
                $notMatchvalue = $row['sender_address'];

                $sender_address = '<span>'.$row['sender_address'].'</span>';

                // array_push($notMatchvalue, $sender_address);
            }else{
                $notMatchvalue = '<a href="javscript:;" data-toggle="modal" data-target="#viewSenderAddress" data-id="'.$row['id'].'"  title="View Sender Address" class="viewTestedBrand"><i class="fa fa-eye text-warning"></i></a>';
                $sender_address = '<a href="javscript:;"  data-id="'.$row['id'].'"  title="View Sender Address" class="bg-danger text-white p-3">'.$row['sender_address'].'</a>';

            }
            $actionhtml  = '';
            $i++;
            $nestedData = array();
            $nestedData[] = $i;
            $nestedData[] = date_time_formate($row['event_time']);
            $nestedData[] = $row['operator'] == '' ? 'N/A' : $row['operator'] ;
            $nestedData[] =  $notMatchvalue;
            $nestedData[] = $sender_address;
            $nestedData[] = $row['recipient_msisdn'];
            $nestedData[] = $row['sccp_gt'];
            $nestedData[] = $row['status'];
            $nestedData[] = $row['received_content'];
            $data[] = $nestedData;
        }
        $json_data = array(
            "draw" => intval($requestData['draw']), // for every request/draw by clientside , they send a number as a parameter, when they recieve a response/data they first check the draw number, so we are sending same number in draw.
            "recordsTotal" => intval($totalData), // total number of records
            "recordsFiltered" => intval($totalFiltered), // total number of records after searching, if there is no searching then totalFiltered = totalData
            "data" => $data   // total data array
        );
        return $json_data;
    }

    public function mobiel_report_getdatatable($data_array)
    {
        $requestData = $_REQUEST;
        $columns = array(
            0 => 'result_reports.id',
            1 => 'result_reports.event_time',
            2 => 'mobile_number.operator',
            3 => 'result_reports.sender_address',
            4 => 'result_reports.sender_address',
            5 => 'result_reports.recipient_msisdn',
            6 => 'result_reports.sccp_gt',
            // 7 => 'result_reports.status',
            7 => 'result_reports.received_content',
        );

        $query = Resultreport ::from('result_reports')
                ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id')
                ->where('result_reports.uuid', '!=', null)
                ->where('result_reports.smsid', '!=', null);


        if($data_array['operator'] != 'all'){
            $query->where('mobile_number.operator', $data_array['operator']);
        }

        if($data_array['country_list'] != 'all'){
            $query->where("countries.id", $data_array['country_list']);
        }

        if($data_array['sender_from'] != 'all'){
            $query->where("result_reports.sender_address",$data_array['sender_from']);
        }

        if($data_array['from'] != '' || $data_array['from'] != null ){
            $from = date("Y-m-d",strtotime($data_array['from']));
            $query->whereDate('result_reports.event_time', '>=', $from);
        }

        if($data_array['to'] != '' || $data_array['to'] != null ){
            $to = date("Y-m-d",strtotime($data_array['to']));
            $query->whereDate('result_reports.event_time', '<=', $to);
        }

        if (!empty($requestData['search']['value'])) {   // if there is a search parameter, $requestData['search']['value'] contains search parameter
            $searchVal = $requestData['search']['value'];
            $query->where(function($query) use ($columns, $searchVal, $requestData) {
                $flag = 0;
                foreach ($columns as $key => $value) {
                    $searchVal = $requestData['search']['value'];
                    if ($requestData['columns'][$key]['searchable'] == 'true') {
                        if ($flag == 0) {
                            $query->where($value, 'like', '%' . $searchVal . '%');
                            $flag = $flag + 1;
                        } else {
                            $query->orWhere($value, 'like', '%' . $searchVal . '%');
                        }
                    }
                }
            });
        }

        $temp = $query->orderBy($columns[$requestData['order'][0]['column']], $requestData['order'][0]['dir']);

        $totalData = count($temp->get());
        $totalFiltered = count($temp->get());

        $resultArr = $query->skip($requestData['start'])
                    ->take($requestData['length'])
                    ->select('result_reports.id', 'brand_entry.brand_name',  'result_reports.event_time', 'mobile_number.operator', 'result_reports.brand', 'result_reports.sender_address', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'result_reports.status', 'result_reports.received_content')
                    ->get();



        $data = array();
        $i = 0;

        foreach ($resultArr as $row) {

            $received_content = strtoupper($row['received_content']);
            $senders_address = strtoupper($row['sender_address']);

            // if (str_contains($received_content, $senders_address)) {
            //     $notMatchvalue = $row['sender_address'];

            //     $sender_address = '<span>'.$row['sender_address'].'</span>';
            // }else{
            //     $sender_address = '<a href="javscript:;" data-toggle="modal" data-target="#viewSenderAddress" data-id="'.$row['id'].'"  title="View Sender Address" class="bg-danger text-white p-3 viewSenderAddress">'.$row['sender_address'].'</a>';

            //     $likeString = '"Mobile Number": '.$row['mobile_number'];

            //     $brnadList = Usersreport::from('users_report')
            //                 ->where('users_report.response', 'like', '%'.$likeString.'%')
            //                 ->whereDate('users_report.created_at', date('Y-m-d', strtotime($row['event_time'])))
            //                 ->select('users_report.response', 'users_report.id')
            //                 ->get()
            //                 ->toArray();

            //                 $response = json_decode($brnadList[0]['response']);
            //                 $brandList = [];
            //                 foreach ($response as $res_key => $res_value){
            //                     foreach ($res_value[0] as $key => $value){
            //                         array_push($brandList, strtolower($key));
            //                     }
            //                 }

            //                 // $data = strtolower(implode(',',$brandList));

            //                 $checkReport  = Resultreport::from('result_reports')
            //                             // ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
            //                             ->where('result_reports.recipient_msisdn', $row['recipient_msisdn'])
            //                             ->whereDate('result_reports.event_time',  date('Y-m-d', strtotime($row['event_time'])))
            //                             ->select('result_reports.id', 'result_reports.sender_address', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt')
            //                             ->get()
            //                             ->toArray();

            //                             $senderAddress = [];

            //                             foreach($checkReport as $cr_key => $cs_value){
            //                                 array_push($senderAddress, strtolower($cs_value['sender_address']));

            //                             }
            //                             // ccd($senderAddress);

            //                             // $notMatchvalue = [];
            //                             foreach($brandList as $sa_key => $sa_value){
            //                                 // ccd($sa_value);
            //                                 if(in_array($sa_value, $senderAddress)){

            //                                     // $data = $sa_value;
            //                                     // array_push($notMatchvalue, $sa_value);
            //                                 }else{

            //                                     $notMatchvalue = '<a href="javscript:;" data-toggle="modal" data-target="#viewTestedBrand" data-id="'.$row['id'].'"  title="View Sender Address" class="btn btn-icon viewTestedBrands"><i class="fa fa-eye text-warning" title="Edit Brand Entry"> </i></a>';
            //                                 //    array_push($notMatchvalue, $sa_value);

            //                                 }
            //                             }
            // }

            if (str_contains($received_content, $senders_address)) {
                $notMatchvalue = $row['sender_address'];

                $sender_address = '<span>'.$row['sender_address'].'</span>';

                // array_push($notMatchvalue, $sender_address);
            }else{
                $notMatchvalue = '<a href="javscript:;" data-toggle="modal" data-target="#viewSenderAddress" data-id="'.$row['id'].'"  title="View Sender Address" class="viewTestedBrand"><i class="fa fa-eye text-warning"></i></a>';

                // $notMatchvalue = '<a href="javscript:;" data-toggle="modal" data-target="#viewSenderAddress" data-id="'.$row['id'].'"  title="View Sender Address" class="viewTestedBrand"><i class="fa fa-eye text-warning"></i></a>';
                $sender_address = '<a href="javscript:;"  data-id="'.$row['id'].'"  title="View Sender Address" class="bg-danger text-white p-3">'.$row['sender_address'].'</a>';

            }

            $actionhtml  = '';
            $i++;
            $nestedData = array();
            $nestedData[] = $i;
            $nestedData[] = date_time_formate($row['event_time']);
            $nestedData[] = $row['operator'] == '' ? 'N/A' : $row['operator'] ;
            $nestedData[] = $notMatchvalue;
            $nestedData[] = $sender_address;
            $nestedData[] = $row['recipient_msisdn'];
            $nestedData[] = $row['sccp_gt'];
            // $nestedData[] = $row['status'];
            $nestedData[] = $row['received_content'];
            $data[] = $nestedData;
        }
        $json_data = array(
            "draw" => intval($requestData['draw']), // for every request/draw by clientside , they send a number as a parameter, when they recieve a response/data they first check the draw number, so we are sending same number in draw.
            "recordsTotal" => intval($totalData), // total number of records
            "recordsFiltered" => intval($totalFiltered), // total number of records after searching, if there is no searching then totalFiltered = totalData
            "data" => $data   // total data array
        );
        return $json_data;
    }

    public function update_report(){
        $logindata = Auth()->guard('admin')->user();

        $xmlString = file_get_contents(public_path('/backend_automation/'.$logindata['first_name']."_".$logindata['last_name']."_".$logindata['user_no'].'/sample.xml'));

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
    }

    public function get_sender_chat(){
        $res = Resultreport::from('result_reports')
                        ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                        ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                        ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id')
                        ->where('result_reports.uuid', null)
                        ->where('result_reports.smsid', null)                        
                        ->groupBy('result_reports.sender_address')
                        ->select('result_reports.sender_address', DB::raw('COUNT(result_reports.id)as count'),)
                        ->get()
                        ->toArray();
                        
        $data['sender'] = [];
        $data['count'] = [];
        foreach($res as $key => $value){
            array_push($data['sender'], $value['sender_address']);
            array_push($data['count'], $value['count']);
        }

        return $data;
    }

    public function get_sender_chat_mobile_report(){
        $res = Resultreport::from('result_reports')
                        ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                        ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                        ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id')
                        ->where('result_reports.uuid', '!=', null)
                        ->where('result_reports.smsid', '!=', null)
                        ->groupBy('result_reports.sender_address')
                        ->select('result_reports.sender_address', DB::raw('COUNT(result_reports.id)as count'),)
                        ->get()
                        ->toArray();
        $data['sender'] = [];
        $data['count'] = [];
        foreach($res as $key => $value){
            array_push($data['sender'], $value['sender_address']);
            array_push($data['count'], $value['count']);
        }

        return $data;
    }

    public function get_sender_chat_result(){
        $res_type = Resultreport::from('result_reports')
                        ->groupBy('result_reports.status')
                        ->select('result_reports.status')
                        ->get()
                        ->toArray();

        $data = collect(range(11, 0));

        $details = [];
        $month_array = [];
        $result_value = [];
        $temp_array = [];
        foreach($res_type as $res_key => $res_value){
            array_push($result_value, $res_value['status']);
        }

        foreach($data as $key => $value){
            $dt = today()->startOfMonth()->subMonth($value);
            $month_name = $dt->shortMonthName."-".$dt->format('Y');
            $date = '01-'.$month_name;
            array_push($month_array, $month_name);


            foreach($res_type as $res_key => $res_value){
                $count = Resultreport::from('result_reports')
                            ->where('result_reports.result_value', $res_value['result_value'])
                            ->whereMonth('result_reports.event_time', date('m', strtotime($date)))
                            ->count();
            }

        }
        // $result_value['name'] = ["Allowed", "Not Allowed"] ;
        $result_value = [
            [
                'name'=> 'Allowed',
                'data' => ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60'],
            ],
            [
                'name'=> 'Not Allowed',
                'data' => ['60', '55', '31', '23', '45', '77', '74', '85', '12', '45', '78', '45'],
            ],

        ];
        $details['month'] = $month_array;
        $details['result_value'] = $result_value;
        return $details;
    }

    public function get_sender_sender_from(){
        return Resultreport::where('result_reports.uuid', null)
                        ->where('result_reports.smsid', null)
                        ->groupBy('result_reports.sender_address')
                        ->select('result_reports.sender_address')
                        ->get()
                        ->toArray();
    }

    public function get_sender_sender_from_mobile_report(){
        return Resultreport::where('result_reports.uuid', '!=', null)
                        ->where('result_reports.smsid', '!=', null)
                        ->groupBy('result_reports.sender_address')
                        ->select('result_reports.sender_address')
                        ->get()
                        ->toArray();
    }

    public function get_sender_result_value(){
        return Resultreport::groupBy('result_reports.status')
                        ->select('result_reports.status')
                        ->get()
                        ->toArray();
    }

    public function download_excel_download($from, $to, $sender_from, $operator, $country_list){

        $query = Resultreport ::from('result_reports')
                    ->where('result_reports.uuid', null)
                    ->where('result_reports.smsid', null)
                    ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                    ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                    ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id');

                if($operator != 'all'){
                    $query->where('mobile_number.operator', $operator);
                }

                if($country_list != 'all'){
                    $query->where("countries.id", $country_list);
                }

                if($sender_from != 'all'){
                    $query->where("result_reports.sender_address",$sender_from);
                }

                if($from != '' || $from != null ){
                    $from = date("Y-m-d",strtotime($from));
                    $query->whereDate('result_reports.event_time', '>=', $from);
                }

                if($to != '' || $to != null ){
                    $to = date("Y-m-d",strtotime($to));
                    $query->whereDate('result_reports.event_time', '<=', $to);
                }

        $result = $query->select('result_reports.id', 'result_reports.event_time', 'result_reports.sender_address', 'mobile_number.operator', 'result_reports.brand', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'result_reports.status', 'result_reports.received_content', 'mobile_number.mobile_number')
                        ->get();

        return  $result;
    }

    public function download_excel_mobile_report($from, $to, $sender_from, $operator, $country_list){

        $query = Resultreport ::from('result_reports')
                    ->where('result_reports.uuid', '!=', null)
                    ->where('result_reports.smsid', '!=', null)
                    ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
                    ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                    ->leftjoin('countries', 'countries.id', '=', 'mobile_number.country_id');

                if($operator != 'all'){
                    $query->where('mobile_number.operator', $operator);
                }

                if($country_list != 'all'){
                    $query->where("countries.id", $country_list);
                }

                if($sender_from != 'all'){
                    $query->where("result_reports.sender_address",$sender_from);
                }

                if($from != '' || $from != null ){
                    $from = date("Y-m-d",strtotime($from));
                    $query->whereDate('result_reports.event_time', '>=', $from);
                }

                if($to != '' || $to != null ){
                    $to = date("Y-m-d",strtotime($to));
                    $query->whereDate('result_reports.event_time', '<=', $to);
                }

        $result = $query->select('result_reports.id', 'result_reports.event_time', 'result_reports.sender_address', 'mobile_number.operator', 'result_reports.brand', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'result_reports.status', 'result_reports.received_content')
                        ->get();

        return  $result;
    }

    public function view_tested_brand($requestData){

        $reportDetails  = Resultreport::from('result_reports')
                            ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                            ->where('result_reports.id', $requestData['reportId'])
                            ->select('result_reports.id', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'mobile_number.mobile_number')
                            ->get()
                            ->toArray();
        $likeString = '"Mobile Number": '.$reportDetails[0]['mobile_number'];
        
                            // "Mobile Number": 9016250108
        $brnadList = Usersreport::from('users_report')
                        ->where('users_report.response', 'like', '%'.$likeString.'%')
                        ->whereDate('users_report.created_at', date('Y-m-d', strtotime($reportDetails[0]['event_time'])))
                        ->select('users_report.response', 'users_report.id')
                        ->get()
                        ->toArray();

        $response = json_decode($brnadList[0]['response']);
        
        $brandList = [];
        foreach ($response as $res_key => $res_value){
            foreach ($res_value[0] as $key => $value){
                array_push($brandList, $key);
            }
        }
        return $brandList;
    }

    public function view_sender_address($requestData){
                    $reportDetails  = Resultreport::from('result_reports')
                    ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                    ->where('result_reports.id', $requestData['reportId'])
                    ->select('result_reports.id', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'mobile_number.mobile_number')
                    ->get()
                    ->toArray();

            $likeString = '"Mobile Number": '.$reportDetails[0]['mobile_number'];

            $brnadList = Usersreport::from('users_report')
                        ->where('users_report.response', 'like', '%'.$likeString.'%')
                        ->whereDate('users_report.created_at', date('Y-m-d', strtotime($reportDetails[0]['event_time'])))
                        ->select('users_report.response', 'users_report.id')
                        ->get()
                        ->toArray();

                        $response = json_decode($brnadList[0]['response']);
                        $brandList = [];
                        foreach ($response as $res_key => $res_value){
                            foreach ($res_value[0] as $key => $value){
                                array_push($brandList, strtolower($key));
                            }
                        }

                        // $data = strtolower(implode(',',$brandList));

                        $checkReport  = Resultreport::from('result_reports')
                                    // ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                                    ->where('result_reports.recipient_msisdn', $reportDetails[0]['recipient_msisdn'])
                                    ->whereDate('result_reports.event_time',  date('Y-m-d', strtotime($reportDetails[0]['event_time'])))
                                    ->select('result_reports.id', 'result_reports.sender_address', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt')
                                    ->get()
                                    ->toArray();

                                    $senderAddress = [];

                                    foreach($checkReport as $cr_key => $cs_value){
                                        array_push($senderAddress, strtolower($cs_value['sender_address']));

                                    }
                                    // ccd($senderAddress);

                                    $notMatchvalue = [];
                                    foreach($brandList as $sa_key => $sa_value){
                                        // ccd($sa_value);
                                        if(in_array($sa_value, $senderAddress)){

                                            // $data = $sa_value;
                                            // array_push($notMatchvalue, $sa_value);
                                        }else{
                                           array_push($notMatchvalue, $sa_value);

                                        }
                                    }
                                    return $notMatchvalue;

    }

    public function get_tested_brand($mobile_number, $event_time, $recipient_msisdn, $received_content, $sender_address, $id){

        $received_content = strtoupper($received_content);
            $senders_address = strtoupper($sender_address);

            if (str_contains($received_content, $senders_address)) {
                $data = [];
                $sender_add = $sender_address;
                array_push($data, $sender_add);

                return $data;
            }else{
                $brandList = [];
                  $reportDetails  = Resultreport::from('result_reports')
                            ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
                            ->where('result_reports.id', $id)
                            ->select('result_reports.id', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt', 'mobile_number.mobile_number')
                            ->get()
                            ->toArray();

                if($reportDetails){
                    $likeString = '"Mobile Number": '.$reportDetails[0]['mobile_number'];
                                    // "Mobile Number": 9016250108
                    $brnadList = Usersreport::from('users_report')
                                    ->where('users_report.response', 'like', '%'.$likeString.'%')
                                    ->whereDate('users_report.created_at', date('Y-m-d', strtotime($reportDetails[0]['event_time'])))
                                    ->select('users_report.response', 'users_report.id')
                                    ->get()
                                    ->toArray();
                    if($brnadList){
                        // $response = $brnadList[0]['response'];
                        $response = json_decode($brnadList[0]['response']);
                        foreach ($response as $res_key => $res_value){
                            foreach ($res_value[0] as $key => $value){
                                array_push($brandList, $key);
                            }
                        }
                    }

                }


                return $brandList;
            //     $likeString = '"Mobile Number": '.$mobile_number;

            // $brnadList = Usersreport::from('users_report')
            //             ->where('users_report.response', 'like', '%'.$likeString.'%')
            //             ->whereDate('users_report.created_at', date('Y-m-d', strtotime($event_time)))
            //             ->select('users_report.response', 'users_report.id')
            //             ->get()
            //             ->toArray();

            //             $response = json_decode($brnadList[0]['response']);
            //             $brandList = [];
            //             foreach ($response as $res_key => $res_value){
            //                 foreach ($res_value[0] as $key => $value){
            //                     array_push($brandList, strtolower($key));
            //                 }
            //             }

            //             // $data = strtolower(implode(',',$brandList));

            //             $checkReport  = Resultreport::from('result_reports')
            //                         // ->join('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
            //                         ->where('result_reports.recipient_msisdn', $recipient_msisdn)
            //                         ->whereDate('result_reports.event_time',  date('Y-m-d', strtotime($event_time)))
            //                         ->select('result_reports.id', 'result_reports.sender_address', 'result_reports.event_time', 'result_reports.recipient_msisdn', 'result_reports.sccp_gt')
            //                         ->get()
            //                         ->toArray();

            //                         $senderAddress = [];

            //                         foreach($checkReport as $cr_key => $cs_value){
            //                             array_push($senderAddress, strtolower($cs_value['sender_address']));

            //                         }
            //                         // ccd($senderAddress);

            //                         $notMatchvalue = [];
            //                         foreach($brandList as $sa_key => $sa_value){
            //                             // ccd($sa_value);
            //                             if(in_array($sa_value, $senderAddress)){

            //                                 // $data = $sa_value;
            //                                 // array_push($notMatchvalue, $sa_value);
            //                             }else{
            //                             array_push($notMatchvalue, $sa_value);

            //                             }
            //                         }
            //                         return $notMatchvalue;
                // $sender_address = 'Not Found';

                // $sender_address = '<span class="bg-danger text-white p-3">'.$row['sender_address'].'</span>';
            }


    }
}
