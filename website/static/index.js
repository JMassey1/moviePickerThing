$(document).ready(function () {
$('#movieTable').DataTable( {
    'orderMulti': false,

    'columnDefs': [
        {'visible': false, 'targets':[4,5], 'searchable': false},
        {'orderData': [4], 'targets':[3]},
        {'orderData': [5], 'targets':[2]},
        {'order': [[2, 'dec']]}
    ],
    stateSave: true
});

$('.dataTables_length').addClass('bs-select');
});

$(document).ready(function () {
$('#songTable').DataTable( {
    'orderMulti': false,

    'columnDefs': [
        {'visible': false, 'targets':[5,6], 'searchable': false},
        {'orderData': [5], 'targets':[4]},
        {'orderData': [6], 'targets':[3]},
        {'order': [[3, 'dec']]}
    ],
    stateSave: true
})
})

$(document).ready(function () {
    $('.alert').fadeTo(2500,500).slideUp(1000, function() {
        $('.alert').slideUp(500);
    });
});