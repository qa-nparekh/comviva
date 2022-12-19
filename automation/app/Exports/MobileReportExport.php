<?php

namespace App\Exports;

use App\Models\Brandentry;
use Maatwebsite\Excel\Concerns\FromCollection;
use Maatwebsite\Excel\Concerns\FromArray;
use Maatwebsite\Excel\Concerns\WithHeadings;
use Maatwebsite\Excel\Concerns\ShouldAutoSize;
use Maatwebsite\Excel\Concerns\WithColumnFormatting;
use PhpOffice\PhpSpreadsheet\Style\NumberFormat;
use App\Models\Resultreport;

class MobileReportExport implements FromArray, WithHeadings, ShouldAutoSize, WithColumnFormatting
{
    /**
    * @return \Illuminate\Support\Collection
    */
    public function __construct($data)
    {
        // ccd($data);
        $this->from = $data['from'];
        $this->to = $data['to'];
        $this->operator = $data['operator'];
        $this->country_list = $data['country_list'];
        $this->sender_from = $data['sender_from'];
    }

    public function array(): array
    {


        $objResultreport = new Resultreport();
        $res = $objResultreport->download_excel_mobile_report($this->from, $this->to, $this->sender_from, $this->operator, $this->country_list);

        $data = [];
        $i = 1;
        foreach($res as $key => $value){
            $daat = get_tested_brand($value['mobile_number'], $value['event_time'], $value['recipient_msisdn'], $value['received_content'], $value['sender_address'], $value['id']);
            $data[$key]['srno'] = $i;
            $data[$key]['event_time'] = date_time_formate($value['event_time']);
            $data[$key]['operator'] = $value['operator'];
            $data[$key]['brand'] =implode(',' ,$daat);
            $data[$key]['sender_address'] =$value['sender_address'];
            $data[$key]['recipient_msisdn'] = $value['recipient_msisdn'];
            $data[$key]['sccp_gt'] = $value['sccp_gt'];
            // $data[$key]['status'] = $value['status'];
            $data[$key]['received_content'] = $value['received_content'];
            $i++;
        }

        return $data;
    }

    public function headings(): array
    {
        return [
            'Sr. No',
            'Time Stamp',
            'Operator',
            'Tested Brand',
            'Sender Address',
            'Recipient MSISDN',
            'SCCP GT',
            // 'Status',
            'Received Content'
        ];
    }

    public function columnFormats(): array
    {
        return [
            'A' => NumberFormat::FORMAT_TEXT,
            'B' => NumberFormat::FORMAT_TEXT,
            'C' => NumberFormat::FORMAT_TEXT,
            'D' => NumberFormat::FORMAT_TEXT,
            'E' => NumberFormat::FORMAT_NUMBER,
            'F' => NumberFormat::FORMAT_NUMBER,
            'G' => NumberFormat::FORMAT_TEXT,
            // 'H' => NumberFormat::FORMAT_TEXT,
            'H' => NumberFormat::FORMAT_TEXT,
        ];
    }
}
