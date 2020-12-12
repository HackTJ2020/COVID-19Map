(function() {
    var cors_api_host = 'cors-anywhere.herokuapp.com';
    var cors_api_url = 'https://' + cors_api_host + '/';
    var slice = [].slice;
    var origin = window.location.protocol + '//' + window.location.host;
    var open = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function() {
        var args = slice.call(arguments);
        var targetOrigin = /^https?:\/\/([^\/]+)/i.exec(args[1]);
        if (targetOrigin && targetOrigin[0].toLowerCase() !== origin &&
            targetOrigin[1] !== cors_api_host) {
            args[1] = cors_api_url + args[1];
        }
        return open.apply(this, args);
    };
})();
(function() {
    console.log("WORKS")

    var margin = { top : 0, left: 0, right: 0, bottom: 0}, height = window.innerHeight, width = window.innerWidth;

    var svg = d3.select("#map").append("svg")
    .attr("height", height + margin.top + margin.bottom)
    .attr("width", width + margin.left + margin.right).append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    d3.queue().defer(d3.json, "https://alpes.cloud/up/85a75c04c899a39451713622f305ba86.json").defer(d3.csv, "csvFiles/abbreviations.csv").await(ready)

    var projection = d3.geoAlbersUsa().translate([width/2, height/2]).scale(window.innerWidth)

    var path = d3.geoPath().projection(projection)

    var states

    function ready(error, data, abbreviations) {
        console.log(data)

        states = topojson.feature(data, data.objects.states).features
        
        console.log(states)

        svg.selectAll(".state").data(states).enter().append("path").attr("class", "state").attr("d", path)

        console.log(abbreviations)
        svg.selectAll(".abbreviation").data(abbreviations).enter().append("text")
        .text(function(d){
            return d.location
        })
        .attr("cx", function(d) {
            var coord = projection(d.long)
            return coord
        })
        .attr("cy", function(d) {
            var coord = projection(d.lat)
            return coord
        })
    }
    
}) ();