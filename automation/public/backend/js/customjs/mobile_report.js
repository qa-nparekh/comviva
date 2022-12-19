var Mobile_report = function(){
    var list = function(){
        $('.select2').select2();

        $("#datepicker_from").datepicker({
            format: 'd-M-yyyy',
            todayHighlight: true,
            autoclose: true,
            orientation: "bottom auto"
        });

        $("#datepicker_to").datepicker({
            format: 'd-M-yyyy',
            todayHighlight: true,
            autoclose: true,
            orientation: "bottom auto"
        });

        $('body').on('click', '#get_data', function(){
            var html = '';
            html = '<table class="table table-bordered table-checkable" id="reports-list">'+
                    '<thead>'+
                    '<th>Sr. No</th>'+
                    '<th>Time Stamp</th>'+
                    '<th>Operator</th>'+
                    '<th>Tested Brand</th>'+
                    '<th>Sender Address</th>'+
                    '<th>Recipient MSISDN</th>'+
                    '<th>SCCP GT</th>'+
                    // '<th>Status</th>'+
                    '<th>Received Content</th>'+
                    '</thead>'+
                    '<tbody>'+
                    '</tbody>'+
                    '</table>';
            $("#reports-list-div").html(html);

            // var result_value = $("#result_value").val();
            var operator = $("#operator").val();
            var country_list = $("#country_list").val();
            var sender_from = $("#sender_from").val();
            var from = $("#datepicker_from").val();
            var to = $("#datepicker_to").val();

            var dataArr = {'sender_from':sender_from, 'from':from, 'to':to, 'operator':operator, 'country_list':country_list};
            var columnWidth = { "width": "5%", "targets": 0 };
            var arrList = {
                'tableID': '#reports-list',
                'ajaxURL': baseurl + "admin/mobile-report-ajaxcall",
                'ajaxAction': 'getdatatable',
                'postData': dataArr,
                'hideColumnList': [],
                'noSortingApply': [0],
                'noSearchApply': [0],
                'defaultSortColumn': [0],
                'defaultSortOrder': 'DESC',
                'setColumnWidth': columnWidth
            };
            getDataTable(arrList);
        });

        $('body').on('click', '.clearSearch', function(){
            var html = '';
            html = '<table class="table table-bordered table-checkable" id="reports-list">'+
                    '<thead>'+
                    '<th>Sr. No</th>'+
                    '<th>Time Stamp</th>'+
                    '<th>Operator</th>'+
                    '<th>Tested Brand</th>'+
                    '<th>Sender Address</th>'+
                    '<th>Recipient MSISDN</th>'+
                    '<th>SCCP GT</th>'+
                    // '<th>Status</th>'+
                    '<th>Received Content</th>'+
                    '</thead>'+
                    '<tbody>'+
                    '</tbody>'+
                    '</table>';
            $("#reports-list-div").html(html);

            $('#result_value').val('all').trigger('change');
            $('#sender_from').val('all').trigger('change');
            $('#datepicker_from').val('');
            $('#datepicker_to').val('');

            var operator = $("#operator").val();
            var country_list = $("#country_list").val();
            var sender_from = $("#sender_from").val();
            var from = $("#datepicker_from").val();
            var to = $("#datepicker_to").val();

            var dataArr = {'sender_from':sender_from, 'from':from, 'to':to, 'operator':operator, 'country_list':country_list};
            var columnWidth = { "width": "5%", "targets": 0 };
            var arrList = {
                'tableID': '#reports-list',
                'ajaxURL': baseurl + "admin/mobile-report-ajaxcall",
                'ajaxAction': 'getdatatable',
                'postData': dataArr,
                'hideColumnList': [],
                'noSortingApply': [0],
                'noSearchApply': [0],
                'defaultSortColumn': [0],
                'defaultSortOrder': 'DESC',
                'setColumnWidth': columnWidth
            };
            getDataTable(arrList);


        });

        $('body').on('click', '#excel_downloads', function(){
            var operator = $("#operator").val();
            var country_list = $("#country_list").val();
            var sender_from = $("#sender_from").val();
            var from = $("#datepicker_from").val();
            var to = $("#datepicker_to").val();

            var dataArr = {'operator' : operator, 'country_list':country_list, 'sender_from':sender_from, 'from':from, 'to':to};
            var url =  baseurl + "admin/download-excel-mobile-report?operator="+operator+"&sender_from="+sender_from+"&from="+from+"&to="+to+"&country_list="+country_list ;
            window.location = url;

        });

        const primary = '#6993FF';
        const success = '#1BC5BD';
        const info = '#8950FC';
        const warning = '#FFA800';
        const danger = '#F64E60';

        var operator = $("#operator").val();
        var country_list = $("#country_list").val();
        var sender_from = $("#sender_from").val();
        var from = $("#datepicker_from").val();
        var to = $("#datepicker_to").val();

        var dataArr = {'sender_from':sender_from, 'from':from, 'to':to, 'operator':operator, 'country_list':country_list};

        var columnWidth = { "width": "5%", "targets": 0 };
        var arrList = {
            'tableID': '#reports-list',
            'ajaxURL': baseurl + "admin/mobile-report-ajaxcall",
            'ajaxAction': 'getdatatable',
            'postData': dataArr,
            'hideColumnList': [],
            'noSortingApply': [0],
            'noSearchApply': [0],
            'defaultSortColumn': [0],
            'defaultSortOrder': 'DESC',
            'setColumnWidth': columnWidth
        };
        getDataTable(arrList);

        $.ajax({
            type: "POST",
            headers: {
                'X-CSRF-TOKEN': $('input[name="_token"]').val(),
            },
            url: baseurl + "admin/mobile-report-ajaxcall",
            data: { 'action': 'sender-chat'},
            success: function(data) {
                $("#loader").show();
                var output = JSON.parse(data);
                const apexChart = "#sender_chat";
                var options = {
                    series: output.count,
                    labels: output.sender,
                    chart: {
                        width: 550,
                        type: 'donut',
                    },
                    responsive: [{
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 350
                            },
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }],
                    legend: {
                        position: 'top'
                    },
                    colors: [primary, success, warning, danger, info]
                };

                var chart = new ApexCharts(document.querySelector(apexChart), options);
                chart.render();
            },
            complete: function(){
                $("#loader").hide();
            }
        });

        $('body').on('click', '.viewSenderAddress', function(){
            $("#loader").show();
            var reportId = $(this).attr('data-id');
            $.ajax({
                type: "POST",
                headers: {
                    'X-CSRF-TOKEN': $('input[name="_token"]').val(),
                },
                url: baseurl + "admin/mobile-report-ajaxcall",
                data: { 'action': 'view-sender-address', 'reportId' : reportId },
                success: function(data) {
                    $("#loader").show();
                    var output = JSON.parse(data);
                    var html = '';
                    for(var i = 0 ; i < output.length ; i++){
                        html =  html + '<p>'+ output[i] +'</p>';
                    }
                    $("#view-sender-address").html(html);
                },
                complete: function(){
                    $("#loader").hide();
                }
            });
        });

        $('body').on('click', '.viewTestedBrand', function(){
            var html = '';
            $("#view-sender-address").html(html);
            $("#loader").show();
            var reportId = $(this).attr('data-id');
            $.ajax({
                type: "POST",
                headers: {
                    'X-CSRF-TOKEN': $('input[name="_token"]').val(),
                },
                url: baseurl + "admin/mobile-report-ajaxcall",
                data: { 'action': 'view-tested-brand', 'reportId' : reportId },
                success: function(data) {
                    $("#loader").show();
                    var output = JSON.parse(data);
                    var html = '';

                    for(var i = 0 ; i < output.length ; i++){
                        html =  html + '<p>'+ output[i] +'</p>';
                    }
                    // console.log(html);
                    $("#view-sender-address").html(html);
                },
                complete: function(){
                    $("#loader").hide();
                }
            });
        });

    }

    return {
        init: function(){
            list();
        }
    }
}();
