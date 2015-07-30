

function Search() {
    searchbox = document.getElementById("search");
    SearchQuery = searchbox.value;
    if (searchbox.value == "") {
        structure = "";
    }
    return ViewType(SearchQuery);
} 



function ViewType(SearchQuery) {


    $.getJSON("/api/users/" + Team + "/?search=" + SearchQuery + "&t=" + +new Date(),
    function (data) {
    if (document.getElementById("tbodytag") && !Append && DivToAppendTo == null) {
        $('#tbodytag').remove();
    }
    var items = [];
    $.each(data, function (key, value) {
    	items.push('<li id="user' + value["id"] + '"><div class="large-1 columns"><img src="http://localhost:8000/static/img/default.png"></div><div class="large-4 columns">' + value.first_name + ' ' + value.last_name + '</div><div class="large-5 columns">' + value.email + '</div><div class="large-2 columns"><a href="#" class="poll-edit" onclick="Invite(' + value["id"] +')">Invite</a></div>' + '</li>')
    });
    console.log(items)
    $('#search-results').html(items)
  });
}
function escapeHtml(string) {
    return String(string).replace(/[&<>"'\/]/g, function (s) {
        return entityMap[s];
    });
}