$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    $(data.results).each(function (i, value) { 
         $("ul#list_movies").append("<li>" + value.title + "</li>");
    });
    
});