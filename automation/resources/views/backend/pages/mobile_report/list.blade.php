@extends('backend.layout.layout')
@section('section')

<!--begin::Entry-->
<div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <div class="container-fluid">
        @csrf

        <div class="row">
            <div class="col-lg-12">
                <!--begin::Card-->
                <div class="card card-custom gutter-b">
                    <div class="card-header">
                        <div class="card-title">
                            <h3 class="card-label">List Of Sender</h3>
                        </div>
                    </div>
                    <div class="card-body" style="height: 500px !important;">
                        <!--begin::Chart-->
                        <div id="sender_chat" class="d-flex justify-content-center"></div>
                        <!--end::Chart-->
                    </div>
                </div>
                <!--end::Card-->
            </div>

        </div>

        <!--begin::Card-->
        <div class="card card-custom gutter-b">
            <div class="card-header flex-wrap py-3">

                <div class="card-title">
                    <h3 class="card-label">{{ $header['title'] }}</h3>
                </div>

                {{-- <div class="card-toolbar">
                    <a href="{{ route('update-report') }}" class="btn btn-primary font-weight-bolder mr-5 update-records">
                        Update Report
                    </a>
                </div> --}}
            </div>

            <div class="card-body">
                <div class="row">

                    <div class="col-md-2">
                        <div class="form-group">
                            <label>Operator</label>
                            <select class="form-control select2 operator" id="operator"  name="operator">
                                <option value="all">All</option>
                                @foreach ($operator_list as $key => $value )
                                    <option value="{{ $value['operator'] }}" >{{ $value['operator'] }}</option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="col-md-2">
                        <div class="form-group">
                            <label>Country</label>
                            <select class="form-control select2 country_list" id="country_list"  name="country_list">
                                <option value="all">All</option>
                                @foreach ($country_list as $key => $value )
                                    <option value="{{ $value['id'] }}" >+{{ $value['phonecode'] }} - {{ $value['name'] }}</option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="col-md-2">
                        <div class="form-group">
                            <label>Brand</label>
                            <select class="form-control select2 sender_from" id="sender_from"  name="sender_from">
                                <option value="all">All</option>
                                @foreach ($sender_from as $key => $value )
                                    <option value="{{ $value['sender_address'] }}" >{{ $value['sender_address'] }}</option>
                                @endforeach
                            </select>
                        </div>
                    </div>

                    <div class="col-md-2">
                        <div class="form-group">
                            <label>Event From</label>
                            <input class="form-control from_date filter-field" name="date" value="" type="text" placeholder="From date" id="datepicker_from" autocomplete="off">
                        </div>
                    </div>

                    <div class="col-md-2">
                        <div class="form-group">
                            <label>Event To</label>
                            <input class="form-control to_date filter-field" name="date" value="" type="text" placeholder="To date" id="datepicker_to" autocomplete="off">
                        </div>
                    </div>

                    <div class="col-md-2">
                        <label>&nbsp;</label>
                        <div class="form-group">
                            <a href="javascript:;" class="btn btn-icon btn-primary search-btn Search" id="get_data">
                                <i class="flaticon-search"></i>
                            </a>

                            <a href="javascript:;"  class="btn btn-icon btn-danger clearSearch" id="clearSearch">
                                <i class="flaticon-cancel"></i>
                            </a>

                            <a href="javascript:;" class="btn btn-icon excel-download" style="background: #1D6F42;" id="excel_downloads" target="_blank">
                                <i class="far fa-file-excel text-white"></i>
                            </a>

                        </div>
                    </div>

                </div>
                <!--begin: Datatable-->
                <div id="reports-list-div">
                    <table class="table table-bordered table-checkable" id="reports-list">
                        <thead>
                            <tr>
                                <th>Sr. No</th>
                                <th>Time Stamp</th>
                                <th>Operator</th>
                                <th>Tested Brand</th>
                                <th>Sender Address</th>
                                <th>Recipient MSISDN</th>
                                <th>SCCP GT</th>
                                {{-- <th>Status</th> --}}
                                <th>Received Content</th>
                            </tr>
                        </thead>
                        <tbody>

                        </tbody>
                    </table>
                </div>
                <!--end: Datatable-->
            </div>
        </div>
        <!--end::Card-->


    </div>
    <!--end::Container-->
</div>
<!--end::Entry-->
<style>

    thead>tr>:nth-child(4){

     text-align:center;
    }
    tbody>tr>:nth-child(4){

     text-align:center;
    }
    </style>
@endsection
