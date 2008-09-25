 $(document).ready(function(){
     var eml = document.getElementById('eml');
     var retrieve = document.getElementById('retrieve');
     $(eml).hide(); $(retrieve).hide();
 })
 
function hl(eid){
    var eid = document.getElementById(eid);
    $(eid).show("fast");
}