$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
});


var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirmPassword");



function confirmLogout(){
    var agree = confirm("Are you sure?");

    if(agree){
        return true;
    } else {
        return false;
    }
}

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
                      <input name='steps' type='text' maxlength='120' required>
                    </div>
                    <a class='remove-list-item'><i class="fas fa-times"></i></a>
                  </li>`;
    $( this ).parent().before(listItem);
});