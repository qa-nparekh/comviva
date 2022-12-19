<?php

namespace App\Http\Controllers\backend\mobile_report;

use App\Exports\MobileReportExport;
use App\Http\Controllers\Controller;
use App\Models\Countries;
use App\Models\Resultreport;
use Illuminate\Http\Request;
use Maatwebsite\Excel\Facades\Excel;
use Config;

class MobilereportController extends Controller
{
    function __construct()
    {
        $this->middleware('admin');
    }

    public function  list(Request $request){

        $objCountries = new Countries();
        $data['operator_list'] = $objCountries->get_filter_operator_list();

        $objCountries = new Countries();
        $data['country_list'] = $objCountries->get_filter_country_list();

        $objResultreport = new Resultreport();
        $data['sender_from'] = $objResultreport->get_sender_sender_from_mobile_report();

        $data['title'] =  Config::get('constants.SYSTEM_NAME') . ' || Mobile Report List';
        $data['description'] =  Config::get('constants.SYSTEM_NAME') . ' || Mobile Report List';
        $data['keywords'] =  Config::get('constants.SYSTEM_NAME') . ' || Mobile Report List';
        $data['css'] = array(
            'toastr/toastr.min.css'
        );
        $data['plugincss'] = array(
            'plugins/custom/datatables/datatables.bundle.css'
        );
        $data['pluginjs'] = array(
            'toastr/toastr.min.js',
            'plugins/custom/datatables/datatables.bundle.js',
            'pages/crud/datatables/data-sources/html.js',
            'pages/features/charts/apexcharts.js'
        );
        $data['js'] = array(
            'comman_function.js',
            'mobile_report.js',
        );
        $data['funinit'] = array(
            'Mobile_report.init()'
        );
        $data['header'] = array(
            'title' => 'Mobile Report List ',
            'breadcrumb' => array(
                'Mobile Report List ' => 'Mobile Report List ',
            )
        );
        return view('backend.pages.mobile_report.list', $data);
    }

    public function download_excel_mobile_report(Request $request){
        if($request->from){
            $data['from'] = $request->from;
        }else{
            $data['from'] = "";
        }

        if($request->to){
            $data['to'] = $request->to;
        }else{
            $data['to'] = "";
        }

        $data['operator'] = $request->operator;
        $data['country_list'] = $request->country_list;
        $data['sender_from'] = $request->sender_from;

        // ccd($data);

        return Excel::download(new MobileReportExport($data), 'Output-'.time().'.xlsx');
    }

    public function ajaxcall(Request $request){
        $action = $request->input('action');
        switch ($action) {
            case 'getdatatable':
                $details = $request->input('data');
                $objResultreport = new Resultreport();
                $list = $objResultreport->mobiel_report_getdatatable($details);

                echo json_encode($list);
                break;

            case 'sender-chat':
                $objResultreport = new Resultreport();
                $data = $objResultreport->get_sender_chat_mobile_report();

                echo json_encode($data);
                break;

            case 'view-tested-brand';
                $objResultreport = new Resultreport();
                $data = $objResultreport->view_tested_brand($request->input());

                echo json_encode($data);
                break;

            case 'view-sender-address';
            // ccd($request->input('data'));
            $objResultreport = new Resultreport();
            $data = $objResultreport->view_sender_address($request->input());

            echo json_encode($data);
            break;


        }
    }
}
