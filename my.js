$(document).ready(
    function () {
    	$.getJSON( "test.json", function( data ) {
    		console.log(data);
    		var json = data;
        	var tr;
        	for (var i = 0; i < json.length; i++) {
            	tr = $('<tr/>');
            	tr.append("<td>" + json[i]["work-summary"][0].title.title.value + "</td>");
            	tr.append("<td>" + json[i]["work-summary"][0]["publication-date"].year.value + "</td>");
            	tr.append("<td>" + json[i]["work-summary"][0]["source"]["source-name"].value + "</td>");
            	tr.append("<td>" + json[i]["external-ids"]["external-id"][0]["external-id-value"] + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	tr.append("<td>" + json[i]["last-modified-date"].value + "</td>");
            	$('table').append(tr);
        	}
		});
});

$('#teste > tbody > tr')
 .find('td')
 .wrapInner('<div style="display: none;" />')
 .parent()
 .find('td > div')
 .slideDown(700, function(){

  var $set = $(this);
  $set.replaceWith($set.contents());

 });