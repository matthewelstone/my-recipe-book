$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.tabs').tabs();
});


var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirmPassword");


// ----- Logout
function confirmLogout(){
    var agree = confirm("Are you sure?");

    if(agree){
        return true;
    } else {
        return false;
    }
}

// ---- Shows the image on upload


$('#image').bind('input', function() {
	$('#imageHolder').attr('src', $(this).val()); 
});


$("#imputImage").bind('input', function(){
    $("#image-preview-image").attr("src", $(this).val());
    console.log(result)
});
			
// ----- Adds steps / ingredients 
$("#ingredients , #steps").on("click", ".remove-list-item", function(event) {
    $(this).parent().remove();
});

$( "#ingredients .add-list-item").click(function(event) {
    let listItem = `<li class='collection-item'>
                    <div class='input-field'>
                      <input name='ingredients' type='text' maxlength='120' required>
                    </div>
                    <a class='remove-list-item'><i class="fas fa-times"></i></a>
                  </li>`;
    $( this ).parent().before(listItem);
});
$( "#steps .add-list-item").click(function(event) {
    let listItem = `<li class='collection-item'>
                    <div class='input-field'>
                      <textarea  name="steps"  class="materialize-textarea"></textarea>
                    </div>
                    <a class='remove-list-item'><i class="fas fa-times"></i></a>
                  </li>`;
    $( this ).parent().before(listItem);
});