$(function(){
    $('.js-create-employee').click(function(){
        var btn=$(this);
        $.ajax(
            {
               url:btn.attr('data-url'),
               type:"get",
               datatype:'json',
               beforeSend:function(){
                $('#modal-book').modal('show');
               },
               success:function(data){
                $("#modal-book .modal-content").html(data.html_form);
               }
               

            }
        );
    });
});

$("#modal-book").on('submit','.js-employee-create-form',function(){
    var form=$(this);
    $.ajax({
        url:form.attr('action'),
        data:form.serialize(),
        type:form.attr('method'),
        datatype:'json',
        success:function(data){
            if(data.form_is_valid){
                // alert("employee created")
                $('#employee-table tbody').html(data.html_employee_list);
                $('#modal-book').modal('hide');

            }
            else{
                $('#modal-book .modal-content').html(data.html_form);
            }


        }

    })
    return false;
});










$(function(){

    var loadForm=function(){
        var btn=$(this);
        $.ajax(
            {
                url:btn.attr('data-url'),
                type:'get',

                datatype:'json',
                beforeSend:function(){
                    $('#modal-book').modal('show');

                },
                success:function(data){
                    $('#modal-book .modal-content').html(data.html_form);
                }
            }
        )
    };


    var saveForm=function(){
        var form=$(this);
        $.ajax({
            url:form.attr('action'),
            data:form.serialize(),
            type:form.attr('method'),
            datatype:'json',
            success:function(data){
                if(data.form_is_valid){
                    // alert("employee created")
                    $('#employee-table tbody').html(data.html_employee_list);
                    $('#modal-book').modal('hide');
    
                }
                else{
                    $('#modal-book .modal-content').html(data.html_form);
                }
    
    
            }
    
        })



        
        return false;

    }
//    //create
//     $('.js-create-employee').click(loadForm);
//     $('#modal-book').on('submit','.js-book-create-form',saveForm);
   
    //update
    $("#employee-table").on('click','.js-update-book',loadForm);
    $("#modal-book").on('submit',".js-book-update-form",saveForm);

    //delete
    $("#employee-table").on("click", ".js-delete-book", loadForm);
    $("#modal-book").on("submit", ".js-book-delete-form", saveForm);
});