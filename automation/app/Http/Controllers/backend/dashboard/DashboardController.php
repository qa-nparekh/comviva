<?php

namespace App\Http\Controllers\backend\dashboard;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Users;
use App\Models\Resultreport;
use App\Models\Countries;
use App\Models\Xmlreport;
use Config;
use LDAP\Result;
use Maatwebsite\Excel\Facades\Excel;
use App\Exports\ReportExport;

class DashboardController extends Controller
{
    function __construct()
    {
        $this->middleware('admin');
    }

    public function dashboard(Request $request){

        $objCountries = new Countries();
        $data['operator_list'] = $objCountries->get_filter_operator_list();

        $objCountries = new Countries();
        $data['country_list'] = $objCountries->get_filter_country_list();

        $objResultreport = new Resultreport();
        $data['sender_from'] = $objResultreport->get_sender_sender_from();

        $data['title'] =  Config::get('constants.SYSTEM_NAME') . ' || dashboard';
        $data['description'] =  Config::get('constants.SYSTEM_NAME') . ' || dashboard';
        $data['keywords'] =  Config::get('constants.SYSTEM_NAME') . ' || dashboard';
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
            'dashboard.js',
        );
        $data['funinit'] = array(
            'Dashboard.init()'
        );
        $data['header'] = array(
            'title' => 'Reports ',
            'breadcrumb' => array(
                'Reports ' => 'Reports ',
            )
        );
        return view('backend.pages.dashboard.dashboard', $data);
    }

    public function upload_xml_report(){
        $data['title'] =  Config::get('constants.SYSTEM_NAME') . ' || Upload XML Report';
        $data['description'] =  Config::get('constants.SYSTEM_NAME') . ' || Upload XML Report';
        $data['keywords'] =  Config::get('constants.SYSTEM_NAME') . ' || Upload XML Report';
        $data['css'] = array(
            'toastr/toastr.min.css'
        );
        $data['plugincss'] = array(            
        );
        $data['pluginjs'] = array(
            'plugins/validate/jquery.validate.min.js',
        );
        $data['js'] = array(
            'comman_function.js',
            'ajaxfileupload.js',
            'jquery.form.min.js',
            'upload_xml_report.js',
        );
        $data['funinit'] = array(
            'Uploadxmlreport.init()'
        );
        $data['header'] = array(
            'title' => 'Upload XML Report',
            'breadcrumb' => array(
                'XML Reports' => route('my-report'),
                'Upload XML Report' => 'Upload XML Report',
            )
        );
        return view('backend.pages.dashboard.upload_xml_report', $data);   
    }

    public function save_upload_xml_report(Request $request){
        $objXmlreport = new Xmlreport();
        $res =  $objXmlreport->save_upload_xml_report($request->all());
        if ($res) {
            $return['status'] = 'success';
            $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
            $return['message'] = 'XML file has been updated successfully.';
            $return['redirect'] = route('my-report');
        } else {
                $return['status'] = 'error';
                $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
                $return['message'] = 'Something goes to wrong';
        }
        echo json_encode($return);
        exit;
    }

    public function update_profile(Request $request){

        $data['title'] = Config::get('constants.SYSTEM_NAME') . ' || Update Profile';
        $data['description'] = Config::get('constants.SYSTEM_NAME') . ' || Update Profile';
        $data['keywords'] = Config::get('constants.SYSTEM_NAME') . ' || Update Profile';
        $data['css'] = array(
            'toastr/toastr.min.css'
        );
        $data['plugincss'] = array(
        );
        $data['pluginjs'] = array(
            'toastr/toastr.min.js',
            'plugins/validate/jquery.validate.min.js',
            'pages/crud/file-upload/image-input.js'
        );
        $data['js'] = array(
            'comman_function.js',
            'ajaxfileupload.js',
            'jquery.form.min.js',
            'dashboard.js',
        );
        $data['funinit'] = array(
            'Dashboard.edit_profile()'
        );
        $data['header'] = array(
            'title' => 'Update Profile',
            'breadcrumb' => array(
                'Reports ' => route('my-report'),
                'Update Profile' => 'Update Profile',
            )
        );
        return view('backend.pages.dashboard.update_profile', $data);
    }

    public function save_profile(Request $request){

        $objUsers = new Users();
        $result = $objUsers->update_profile($request);
        if ($result == "true") {
            $return['status'] = 'success';
             $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
            $return['message'] = 'Your profile successfully updated.';
            $return['redirect'] = route('admin-update-profile');
        } else {
            if ($result == "email_exist") {
                $return['status'] = 'error';
                 $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
                $return['message'] = 'The email address has already been registered.';
            }else{
                $return['status'] = 'error';
                 $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
                $return['message'] = 'Something goes to wrong';
            }
        }
        echo json_encode($return);
        exit;
    }

    public function change_password(Request $request){
        $data['title'] = 'Petrol Station Web Software || Change Password';
        $data['description'] = 'Petrol Station Web Software || Change Password';
        $data['keywords'] = 'Petrol Station Web Software || Change Password';
        $data['css'] = array(
            'toastr/toastr.min.css'
        );
        $data['plugincss'] = array(
        );
        $data['pluginjs'] = array(
            'toastr/toastr.min.js',
            'plugins/validate/jquery.validate.min.js',
            'pages/crud/file-upload/image-input.js'
        );
        $data['js'] = array(
            'comman_function.js',
            'ajaxfileupload.js',
            'jquery.form.min.js',
            'dashboard.js',
        );
        $data['funinit'] = array(
            'Dashboard.change_password()'
        );
        $data['header'] = array(
            'title' => 'Change Password',
            'breadcrumb' => array(
                'Reports ' => route('my-report'),
                'Change Password' => 'Change Password',
            )
        );
        return view('backend.pages.dashboard.change_password', $data);
    }

    public function save_password(Request $request){
        $objUsers = new Users();
        $result = $objUsers->changepassword($request);

        if ($result == "true") {
            $return['status'] = 'success';
            $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
            $return['message'] = 'Your password has been updated successfully.';
            $return['redirect'] = route('admin-change-password');
        } else {
            if ($result == "password_not_match") {
                $return['status'] = 'warning';
                $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
                $return['message'] = 'Your old password is not match.';

                $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';

            }else{
                $return['status'] = 'error';
                $return['jscode'] = '$(".submitbtn:visible").removeAttr("disabled");$("#loader").hide();';
                $return['message'] = 'Something goes to wrong';
            }
        }
        echo json_encode($return);
        exit;
    }

    public function update_report(Request $request){
        $objResultreport = new Resultreport();
        $res = $objResultreport->update_report();
        return redirect()->route('my-report');
    }

    public function download_excel_download(Request $request){
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

        return Excel::download(new ReportExport($data), 'Output-'.time().'.xlsx');
    }

    public function ajaxcall(Request $request){
        $action = $request->input('action');
        switch ($action) {
            case 'getdatatable':
                $details = $request->input('data');
                $objResultreport = new Resultreport();
                $list = $objResultreport->getdatatable($details);

                echo json_encode($list);
                break;

            case 'sender-chat':
                $objResultreport = new Resultreport();
                $data = $objResultreport->get_sender_chat();

                echo json_encode($data);
                break;

            case 'view-tested-brand';
                $objResultreport = new Resultreport();
                $data = $objResultreport->view_sender_address($request->input());

                echo json_encode($data);
                break;

            case 'view-tested-brands';
            $objResultreport = new Resultreport();
            $data = $objResultreport->view_tested_brand($request->input());

            echo json_encode($data);
            break;


        }
    }
}
