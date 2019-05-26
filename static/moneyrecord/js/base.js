$(function(){
    $(".edit-row").hide();
    $(".edit").on("click", function(){
        $(this).toggleClass("clicked");
        if($(this).hasClass("clicked")){
            $(this).parent("div").next("div").show();
        }
        else{
            $(this).parent("div").next("div").hide();
        }
    });
});