var currentORCID = "";

$(document).ready(
    function () {
        $('.list-group').on('click', '.list-group-item', function() {
            localStorage.setItem(currentORCID, $(this).html());
        });
        if($('div').hasClass('mainpages')) {
            $.get("Temp.txt", function( content ) {
                var plain = content.split("\n");
                var as = $("<a/>");
                for(var i = 0; i < plain.length; i++) {
                    as.append("<a href='tabela.html' class=\"list-group-item\">" + plain[i] + "</a>");
                }
                $('.list-group').append(as);
            }, 'text');
        }
        if($('div').hasClass('orcid')) {
        var title = $('<h2>TRABALHOS ACADÉMICOS DE ' + localStorage.getItem(currentORCID) + '</h2>');
        $(title).insertBefore('.container');
    	$.getJSON( "Works_" + localStorage.getItem(currentORCID) + ".json", function( data ) {
    		var json = data;
        	var tr;
        	for (var i = 0; i < json.group.length; i++) {
            	    tr = $('<tr/>');
            	    tr.append("<td>" + json["group"][i]["work-summary"][0].title.title.value + "</td>");
            	    tr.append("<td>" + json["group"][i]["work-summary"][0]["publication-date"].year.value + "</td>");
            	    tr.append("<td>" + json["group"][i]["work-summary"][0]["source"]["source-name"].value + "</td>");
                    var countEID = 0;
                    for (var j = 0; j < json.group[i]["external-ids"]["external-id"].length; j++) {
                        if(json.group[i]["external-ids"]["external-id"][j]["external-id-type"] === "eid")
                            tr.append("<td><a href='tabelascopus.html'>" + json.group[i]["external-ids"]["external-id"][j]["external-id-value"] + "</a></td>");
                        else
                            countEID++;
                    }
                    if (countEID == json.group[i]["external-ids"]["external-id"].length)
                        tr.append("<td>" + "-----" + "</td>");
                    var countWOS = 0;
                    for (var k = 0; k < json.group[i]["external-ids"]["external-id"].length; k++) {
                        if(json.group[i]["external-ids"]["external-id"][k]["external-id-type"] === "wosuid")
                            tr.append("<td>" + json.group[i]["external-ids"]["external-id"][k]["external-id-value"] + "</td>");
                        else
                            countWOS++;
                    }
                    if (countWOS == json.group[i]["external-ids"]["external-id"].length)
                        tr.append("<td>" + "-----" + "</td>");
                    var countDBLP = 0;
                    for (var l = 0; l < json.group[i]["external-ids"]["external-id"].length; l++) {
                        if(json.group[i]["external-ids"]["external-id"][l]["external-id-type"] === "other-id")
                            tr.append("<td>" + json.group[i]["external-ids"]["external-id"][l]["external-id-value"] + "</td>");
                        else
                            countDBLP++;
                    }
                    if (countDBLP == json.group[i]["external-ids"]["external-id"].length)
                        tr.append("<td>" + "-----" + "</td>");
                    if(json.group[i]["work-summary"].length >= 2) {
                        var countISSN = 0;
                        for (var m = 0; m < json.group[i]["work-summary"][1]["external-ids"]["external-id"].length; m++) {
                            if(json.group[i]["work-summary"][1]["external-ids"]["external-id"][m]["external-id-type"] === "issn")
                                tr.append("<td>" + json.group[i]["work-summary"][1]["external-ids"]["external-id"][m]["external-id-value"] + "</td>");
                            else
                                countISSN++;
                        }
                        if (countISSN == json.group[i]["work-summary"][1]["external-ids"]["external-id"].length)
                            tr.append("<td>" + "-----" + "</td>");
                    }
                    else {
                        tr.append("<td>" + "-----" + "</td>");
                    }
            	    $('table').append(tr);
        	}
		});
        $('.success a').click(function() {
            var txt = $(this).text();
            console.log(txt);
        });
    }
    if($('div').hasClass('scopus')) {
        $.getJSON("citations.json", function ( scopus ) {
            console.log(scopus);
            var json = scopus;
            var tr;
            var currentYear = (new Date).getFullYear();
            console.log(currentYear);
            var countCite = 0;
            for(var i = 0; i < json["abstract-citations-response"].citeInfoMatrix.citeInfoMatrixXML.citationMatrix.citeInfo[0]["author"].length; i++) {
                tr = $('<tr/>');
                tr.append("<td>" + json["abstract-citations-response"].citeInfoMatrix.citeInfoMatrixXML.citationMatrix.citeInfo[0]["author"][i]["index-name"] + "</td>");
                tr.append("<td>" + json["abstract-citations-response"].citeColumnTotalXML.citeCountHeader.columnHeading.length + "</td>");
                for(var j = 0; j < json["abstract-citations-response"].citeColumnTotalXML.citeCountHeader.columnHeading.length - 1; j++) {
                    if((currentYear - json["abstract-citations-response"].citeColumnTotalXML.citeCountHeader.columnHeading[j]["$"]) <= 3) {
                        countCite++;
                        j++;
                        console.log(countCite);
                    }
                }
                $('table').append(tr);
            }
        });
    }
});