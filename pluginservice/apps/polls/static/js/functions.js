

function Search() {
    searchbox = document.getElementById("search");
    SearchQuery = searchbox.value;
    if (searchbox.value == "") {
        structure = "";
    }
    return ViewType("/api/users/" + Team + "/?search=" + SearchQuery, null);
} 



function ViewType(SearchQuery, appendto, datastructure) {
    $.getJSON(SearchQuery + "&t=" + +new Date(),
    function (data) {
    var items = [];
    $.each(data, function (key, value) {
        s = '<li id="user{0}">' +
               '<div class="large-1 columns">' +
                   '<img src="http://localhost:8000/static/img/default.png">' +
               '</div>' +
               '<div class="large-4 columns">{1} {2}</div>' +
               '<div class="large-5 columns">{3}</div>' +
               '<div class="large-2 columns">' +
                   '<a href="#" class="poll-edit" onclick="Invite({0})">Invite</a>' +
               '</div>' +
            '</li>';
        items.push(s.format(value["id"], value.first_name, value.last_name, value.email))
    });
    if (appendto == null) {
        $('#search-results').html(items)
    }
    else {
        $(appendto).append(items)
    }
  });

}


function escapeHtml(string) {
    return String(string).replace(/[&<>"'\/]/g, function (s) {
        return entityMap[s];
    });
}

// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}