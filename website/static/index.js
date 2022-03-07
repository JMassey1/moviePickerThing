$(document).ready(function () {
$('#movieTable').DataTable( {
    'columnDefs': [
        {'visible': false, 'targets':[4], 'searchable': false},
        {'orderData': [4], 'targets':[3]},
        {'order': [[2, 'dec']]}
    ],
    stateSave: true
});
$('.dataTables_length').addClass('bs-select');
});

$(document).ready(function () {
$('#songTable').DataTable( {
    'columnDefs': [
        {'visible': false, 'targets':[5], 'searchable': false},
        {'orderData': [5], 'targets':[4]},
        {'order': [[3, 'dec']]}
    ],
    stateSave: true
})
})