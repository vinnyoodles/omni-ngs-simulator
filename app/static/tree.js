var sims = {
    "454Sim":{
        "name":"454Sim",
        "link":"454sim"
    },
    "ART":{
        "name":"ART",
        "link":"ART",
        "parent_dep":true
    },
    "AFG":{
        "name":"AFG",
        "link":"artificial_fastq_generator"
    },
    "BEAR":{
        "name":"BEAR"
    },
    "CuReSim":{
        "name":"CuReSim",
        "link":"curesim"
    },
    "DWGSIM":{
        "name":"DWGSIM",
        "link":"dwgsim"
    },
    "EAGLE":{
        "name":"EAGLE"
    },
    "FASTQSim":{
        "name":"FASTQSim"
    },
    "Flowsim":{
        "name":"Flowsim"
    },
    "GemSim":{
        "name":"GemSim"
    },
    "Grinder":{
        "name":"Grinder"
    },
    "Mason":{
        "name":"Mason",
        "link":"mason",
        "parent_dep":true
    },
    "MetaSim":{
        "name":"MetaSim"
    },
    "NeSSM":{
        "name":"NeSSM"
    },
    "pbsim":{
        "name":"pbsim",
        "link":"pbsim"
    },
    "pIRS":{
        "name":"pIRS",
        "link":"pirs"
    },
    "ReadSim":{
        "name":"ReadSim"
    },
    "simhtsd":{
        "name":"simhtsd"
    },
    "simNGS":{
        "name":"simNGS"
    },
    "SimSeq":{
        "name":"SimSeq"
    },
    "SInC":{
        "name":"SInC"
    },
    "wgsim":{
        "name":"wgsim",
        "link":"wgsim"
    },
    "XS":{
        "name":"XS",
        "link":"xs"
    }
};

function setParent(arr, parent) {
    return arr.slice(0).map(function(obj) { 
        return Object.assign({ parent: parent }, obj);
    });
}

var treeData = window.treeData = [{
    "children": [{
        "name": "Reference sequence",
        "parent": "null",
        "state": false,
        "_children": [{
            "name": "Genomics",
            "_children": [{
                "parent": "Genomics",
                "name": "Genomic variants",
                "_children": [
                { "name": "IonTorrent", "_children": setParent([sims.CuReSim], "IonTorrent")},
                { "name": "SOLiD", "_children": setParent([sims.ART, sims.CuReSim], "SOLiD")},
                { "name": "PacBio", "_children": setParent([sims.pbsim], "PacBio")},
                { "name": "Sanger", "_children": setParent([sims.MetaSim], "Sanger")},
                { "name": "Illumina", "_children": setParent([sims.ART, sims.AFG, sims.MetaSim, sims.simhtsd, sims.simNGS], "Illumina")},
                { "name": "454", "_children": setParent([sims['454sim'], sims.ART, sims.CuReSim, sims.Flowsim, sims.MetaSim, sims.simhtsd], "454")},
                ]
            }, {
                "parent": "Genomics",
                "name": "No genomic variants",
                "_children": [
                { "name": "IonTorrent", "_children":setParent([sims.BEAR, sims.EAGLE, sims.DWGSIM, sims.FASTQSim], "IonTorrent")},
                { "name": "Nanopore", "_children":setParent([sims.ReadSim], "Nanopore")},
                { "name": "SOLiD", "_children":setParent([sims.DWGSIM, sims.FASTQSim, sims.wgsim], "SOLiD")},
                { "name": "PacBio", "_children":setParent([sims.EAGLE, sims.FASTQSim, sims.ReadSim], "PacBio")},
                { "name": "Sanger", "_children":setParent([sims.Grinder, sims.Mason], "Sanger")},
                { "name": "Illumina", "_children":setParent([sims.BEAR, sims.DWGSIM, sims.EAGLE, sims.FASTQSim, sims.GemSim, sims.Grinder, sims.Mason, sims.pIRS, sims.SimSeq, sims.SInC, sims.wgsim], "Illumina")},
                { "name": "454", "_children":setParent([sims.BEAR, sims.EAGLE, sims.GemSim, sims.Grinder, sims.Mason], "454")},
                ]
            }]
        }, {
            "name": "Metagenomics",
            "_children": [{
                "parent": "Metagenomics",
                "name": "Metagenomic variants",
                "_children": [
                { "name": "Sanger", "_children": setParent([sims.MetaSim], "Sanger")},
                { "name": "Illumina", "_children": setParent([sims.MetaSim], "Illumina")},
                { "name": "454", "_children": setParent([sims.MetaSim], "454")},
                ]
            }, {
                "parent": "Metagenomics",
                "name": "No metagenomic variants",
                "_children": [
                { "name": "Illumina" , "_children":setParent([sims.BEAR, sims.FASTQSim, sims.GemSim, sims.Grinder, sims.Mason, sims.NeSSM, sims.pIRS], "Illumina")},
                { "name": "IonTorrent" , "_children":setParent([sims.BEAR, sims.FASTQSim], "IonTorrent")},
                { "name": "454" , "_children":setParent([sims.BEAR, sims.GemSim, sims.Grinder, sims.Mason, sims.NeSSM], "454")},
                { "name": "Sanger" , "_children":setParent([sims.Grinder], "Sanger ")},
                { "name": "SOLiD" , "_children":setParent([sims.FASTQSim], "SOLiD")},
                { "name": "PacBio" , "_children":setParent([sims.FASTQSim], "PacBio")},
                ]
            }]
        }]
    }, {
        "name": "No reference sequence",
        "state": false,
        "_children": [
        { "name": "454" , "_children": setParent([sims.XS], "454")},
        { "name": "IonTorrent" , "_children": setParent([sims.XS], "IonTorrent")},
        { "name": "Illumina" , "_children": setParent([sims.XS], "Illumina")},
        { "name": "SOLiD" , "_children": setParent([sims.XS], "SOLiD")},
        ]
    }]
}];

var margin = {top: 50, right: 200, bottom: 200, left: 200},
width = 1200 - margin.right - margin.left,
height = 800 - margin.top - margin.bottom;

var i = 0,
duration = 750,
root;

var tree = d3.layout.tree()
.size([height, width]);

var diagonal = d3.svg.diagonal()
.projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("body").append("svg")
.attr("width", width + margin.right + margin.left)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = treeData[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);

d3.select(self.frameElement).style("height", "500px");

function update(source) {
    var nodes = tree.nodes(root).reverse(),
    links = tree.links(nodes);

    nodes.forEach(function(d) { d.y = d.depth * 180; });

    var node = svg.selectAll("g.node")
    .data(nodes, function(d) { return d.id || (d.id = ++i); });

    var nodeEnter = node.enter().append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
    .on("click", click);

    nodeEnter.append("circle")
    .attr("r", 1e-6)
    .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeEnter.append("text")
    .attr("x", function(d) { return d.children || d._children ? -13 : 13; })
    .attr("dy", ".35em")
    .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
    .text(function(d) { return d.name; })
    .style("fill-opacity", 1e-6);

    var nodeUpdate = node.transition()
    .duration(duration)
    .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

    nodeUpdate.select("circle")
    .attr("r", 10)
    .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeUpdate.select("text")
    .style("fill-opacity", 1);

    var nodeExit = node.exit().transition()
    .duration(duration)
    .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
    .remove();

    nodeExit.select("circle")
    .attr("r", 1e-6);

    nodeExit.select("text")
    .style("fill-opacity", 1e-6);

    var link = svg.selectAll("path.link")
    .data(links, function(d) { return d.target.id; });

    link.enter().insert("path", "g")
    .attr("class", "link")
    .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
    });

    link.transition()
    .duration(duration)
    .attr("d", diagonal);

    link.exit().transition()
    .duration(duration)
    .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
    })
    .remove();

    nodes.forEach(function(d) {
        d.x0 = d.x;
        d.y0 = d.y;
    });
}

function click(d) {
    if (d.link) {
        var link = d.link;
        if (d.parent) {
            link += '_' + d.parent.name;
        }
        window.location.href = "/omningssimulator/simulators/" + link.toLowerCase();
    }
    if (d.children) {
        d._children = d.children;
        d.children = null;
    } else {
        d.children = d._children;
        d._children = null;
    }
    update(d);
}