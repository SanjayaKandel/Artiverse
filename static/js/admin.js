"use strict";

$(document).ready(function () {
  /*-- sidebar js --*/
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });
  /*-- calendar js --*/
  $('#example14').calendar({
    inline: true
  });
  $('#example15').calendar();
  /*-- tooltip js --*/
  $('[data-toggle="tooltip"]').tooltip();
});

var ps = new PerfectScrollbar('#sidebar');