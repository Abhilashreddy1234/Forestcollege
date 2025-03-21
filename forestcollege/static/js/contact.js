
$(document).ready(function(){
    
    (function($) {
        "use strict";
        $.validator.addMethod("regex",function(value, element, regexp) {
            return this.optional(element) || regexp.test(value);
        },"Please check your input.");
    // validate ContactUsForm form
    $(function() {
        $('#ContactUsForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2,
                    maxlength: 25,
                    regex: /^[a-zA-Z ]*$/
                },
                email: {
                    required: true,
                    email: true
                },
                phone :{
                    required: true,
                    maxlength: 25,
                    regex: /^\+?[\d -]+$/
                },
                subject :{
                    regex: /^[a-zA-Z ]*$/
                },
                messsage :{
                    regex: /^[a-zA-Z ,]*$/
                }

            },
            messages: {
                name: {
                    required: "Name is required",
                    minlength: "Min 2 characters is required",
                    maxlength: "Max 25 characters are allowed",
                    regex: "Only alphabets are allowed"
                },
                email: {
                    required: "Email is required"
                },
                phone: {
                    required: "Phone number required",
                    maxlength: "Max 25 number are allowed",
                    regex: "Only numeric values are allowed"
                },
                subject: {
                    regex: "Special characters are not allowed"
                },
                messsage: {
                    regex: "Special characters are not allowed, except comma (,)"
                }
            },
            errorPlacement: function(error, element) {
                
                    error.insertAfter(element);
            },
            submitHandler: function(form) { //alert(hi);
                // $("#submitBtn").attr("disabled", true);
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url: site_theme_url + "/ContactData.php",
					// url: "localhost/wp-content/themes/fcri/ContactData.php",
                    captcha: grecaptcha.getResponse(),
                    success: function(response) {
                      var responseData = JSON.parse(response);
                        if(responseData.result)
                        {
                            $(".errormsg").html('<span style="color:green;">'+responseData.Message+'</span>').fadeIn().delay(5000).fadeOut();
                            $( '#ContactUsForm' ).each(function(){
                                this.reset();
                                grecaptcha.reset();
                            });
                            $("#submitBtn").attr("disabled", false);
                        }
                        else{
                            $(".errormsg").html('<span style="color:red;">'+responseData.Message+'</span>').fadeIn().delay(5000).fadeOut();
                        }
                    },
                    error: function() {
                    }
                })
            }
        })
    })
 })(jQuery)
})