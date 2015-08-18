

function Search() {
    searchbox = document.getElementById("search");
    SearchQuery = searchbox.value;
    if (searchbox.value == "") {
        structure = "";
    }
    return SearchViewType("/api/users/?inviteable=" + Team + "&search=" + SearchQuery, null, null);
}




function SearchViewType(SearchQuery) {
    $.getJSON(SearchQuery + "&t=" + +new Date(),
	    function (data) {
		    var items = [];
			for (var i = 0; i < data.length; i++) {


		        var datastring = '<li id="user{0}">' +
		               '<div class="large-1 columns">' +
		                   '<img src="http://localhost:8000/static/img/default.png">' +
		               '</div>' +
		               '<div class="large-4 columns">{1} {2}</div>' +
		               '<div class="large-5 columns">{3}</div>' +
		               '<div class="large-2 columns">' +
		                   '<a href="#" class="poll-edit" onclick="Invite({0})">Invite</a>' +
		               '</div>' +
		            '</li>';

				items.push(
					String.format(
						datastring,
						data[i]["id"],
						data[i].first_name,
						data[i].last_name,
						data[i].email
						)
					);

			}
			$('#search-results').html(items)
		});
}


function TeamListUpdate(SearchQuery) {
    $.getJSON("/api/users/" + SearchQuery + "?&t=" + +new Date(),

	    function (data) {
		    var items = [];
		        var datastring = '<li id="userlist{0}"><img src="{1}"><h4>{2} {3}</h4></li>';
		        console.log(data.userprofile);
				items.push(
					String.format(
						datastring,
						data["id"],
						data.userprofile.profile_picture,
						data.first_name,
						data.last_name
						)
					);


			$('#team').append(items)
		});
}



function Notfiy() {
    $.getJSON("/api/notifications/?&t=" + +new Date(), function (data) {
		    var items = [];

		    $.each( data, function( key, val ) {
		        var datastring = '<li id="note{0}"><span>{1} </span> <p>{2}</p></li>';
				items.push(
					String.format(
						datastring,
						val["id"],
						val["title"],
						val["text"]
						)
				);
  			});
			$('#notification').append(items)
		});
}


function GetTeamList(teamid, append) {
    $.getJSON("/api/users/?team=" + teamid + "&t=" + +new Date(), function (data) {
	    var items = [];

	    $.each( data, function( key, val ) {
	        var datastring = '<li><img src="{1}"><h4>{2} {3}</h4></li>';
			items.push(
				String.format(
					datastring,
					val["id"],
					val.userprofile.profile_picture,
					val["first_name"],
					val["last_name"]
					)
			);
			});
			if (append == true) {
			$('#team').append(items)
		}
		else {
			$('#team').html(items)
		}
	});
}

function GetInviteList() {
    $.getJSON("/api/invites/" + "?&t=" + +new Date(), function (data) {
	    var items = [];

	    $.each( data, function( key, val ) {
	        var datastring = '<form action="/team/invitereponse/" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="{0}"><input type="hidden" name="invite_id" value="{1}"><li><span class="left">{2} has invited you to <b>{3}</b></span><span class="right"><input type="submit" name="accept" value="Accept"> <input type="submit" name="accept" value="Decline"></span></li></form>';
			items.push(
				String.format(
					datastring,
					csrf,
					val["id"],
					val.invite_from.username,
					val.team.name
					)
			);
			});
			$('#invites').html(items)
	});
}



function CountInvites() {
    $.getJSON("/api/invites/" + "?&t=" + +new Date(), function (data) {
        var count = 0;

        $.each( data, function( key, val ) {
            count += 1;
        });
        $('.invitesection span').html("(" + count + ")")
    });
}




$(document).ready(function(){

	if (document.getElementById('invites') !== null) {
	  GetInviteList();
      CountInvites();
	}

	if (typeof Team !== 'undefined') {
	  GetTeamList(Team);
    }
})





window.setInterval(function(){

	if (document.getElementById('invites') !== null) {
	  GetInviteList();
      CountInvites();
	}

	if (typeof Team !== 'undefined') {
	  GetTeamList(Team);
    }
}, 5000);









function test() {
	template = new Template({url: 'functions/search.ejs'});
	html = template.render({name: 'My name', age: 26, profession: 'Hacker'});
	return html
}


function escapeHtml(string) {
    return String(string).replace(/[&<>"'\/]/g, function (s) {
        return entityMap[s];
    });
}


if (!String.format) {
  String.format = function(format) {
    var args = Array.prototype.slice.call(arguments, 1);
    return format.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}
