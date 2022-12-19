@extends('backend.layout.layout')
@section('section')

<!--begin::Entry-->
<div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <!--begin::Container-->
    <div class="container-fluid">
       <div class="row">
          <div class="col-md-12">
             <!--begin::Card-->
             <div class="card card-custom gutter-b example example-compact">
                <div class="card-header">
                   <h3 class="card-title">{{ $header['title'] }}</h3>
                </div>
                <!--begin::Form-->
                <form class="form" id="update-xml-report" method="POST" action="{{ route('save-update-xml-report') }}" enctype="multipart/form-data">
                   @csrf
                    <div class="card-body"> 
                        <div class="row">
                            <div class="col-md-12">
                                <div class="form-group">
                                    <label>XML Files
                                    <span class="text-danger">*</span></label>
                                    <input type="file" name="xml_files" class="form-control" placeholder="Please select XML files" accept="text/xml">
                                </div>
                            </div>
                        </div>
                    </div>
 
                    <div class="card-footer">
                        <button type="submit" class="btn btn-primary mr-2 green-btn submitbtn">Submit</button>
                        <button type="reset" class="btn btn-secondary">Cancel</button>
                    </div>
                </form>
                <!--end::Form-->
             </div>
             <!--end::Card-->
          </div>
       </div>
    </div>
    <!--end::Container-->
    <!--end::Container-->
 </div>
 <!--end::Entry-->

@endsection
