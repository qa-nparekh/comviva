var Uploadxmlreport = function(){    
    var uploadFile = function(){        
        var form = $('#update-xml-report');
        var rules = {            
            xml_files: {required: true},
        };
        var message = {            
            xml_files : {
                required : "Please select XML files"
            }
        }
        handleFormValidateWithMsg(form, rules,message, function(form) {
            handleAjaxFormSubmit(form,true);
        });
    }

    return {
        init:function(){
            uploadFile();
        }
    }
}();