<?php

use App\Models\Codenumber;
use App\Models\Device;
use App\Models\Mobilenumber;
use App\Models\Systemsetting;
use App\Models\Users;
use App\Models\Countries;
use App\Models\Resultreport;
use LDAP\Result;

function date_formate($date){
    return date("d-M-Y", strtotime($date));
}

function date_time_formate($date){
    return date("d/m/Y h:i:s A", strtotime($date));
}


function remaing_days($start_date, $end_date){
    return abs(round((strtotime($start_date) - strtotime($end_date)) / (60 * 60 * 24)));
}

function find_date($days, $start_date){
    return date('Y-m-d', strtotime($days." day", strtotime($start_date)));
}

function ccd($value){
    echo "<pre>"; print_r($value); die();
}

function numberformat($value){
    return number_format((float)$value, Config::get('constants.DECIMAL_POINT'), '.', '');
}

function get_no_by_name($no_for){
    $objCodenumber = new Codenumber();
    return $objCodenumber->get_no_by_name($no_for);
}

function auto_increment_no($no_for){
    $objCodenumber = new Codenumber();
    $res = $objCodenumber->auto_increment_no($no_for);
}

function get_system_setting_detail(){
    $objSystemsetting = new Systemsetting();
    return $objSystemsetting->get_system_setting_detail();
}

function get_device_name($id){
    $objDevice = new Device();
    return $objDevice->get_divice_name($id);
}

function get_operator_name($id){
    $objMobilenumber = new Mobilenumber();
    return $objMobilenumber->get_mobile_operator_lists($id);

}

function get_county_code($countryId){
    $objCountries = new Countries();
    return $objCountries->get_county_code($countryId);
}

function get_tested_brand($mobile_number, $event_time, $recipient_msisdn, $received_content, $sender_address, $id){
    $objResulreport = new Resultreport();
    return $objResulreport->get_tested_brand($mobile_number, $event_time, $recipient_msisdn, $received_content, $sender_address, $id);
}


?>
