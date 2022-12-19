<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use PHPUnit\Framework\Constraint\Count;

class Countries extends Model
{
    use HasFactory;
    protected $table = 'countries';

    public function get_countries_details(){
        return Countries::from('countries')
                      ->select('countries.id', 'countries.shortname', 'countries.name', 'countries.phonecode')
                      ->orderBy('countries.phonecode', 'asc')
                      ->orderBy('countries.shortname')
                      ->get()
                      ->toArray();
    }

    public function get_county_code($countryId){
       $result = Countries::where('countries.id', $countryId)
                    ->select('countries.phonecode')
                    ->get()
                    ->toArray();
                    
        return $result[0]['phonecode'];
    }

    public function get_filter_country_list(){
        return Resultreport ::from('result_reports')
            ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
            ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
            ->join('countries', 'countries.id', '=', 'mobile_number.country_id')
            ->select('countries.id', 'countries.shortname', 'countries.phonecode', 'countries.name')
            ->groupBy('mobile_number.country_id')
            ->get()
            ->toArray(); 
    }
   
    public function get_filter_operator_list(){
        return Resultreport ::from('result_reports')
            ->leftjoin('brand_entry', 'brand_entry.brand_name', '=', 'result_reports.brand')
            ->leftjoin('mobile_number', 'mobile_number.number', '=', 'result_reports.recipient_msisdn')
            ->select('mobile_number.operator')
            ->groupBy('mobile_number.operator')
            ->get()
            ->toArray(); 
    }
  
    
}
