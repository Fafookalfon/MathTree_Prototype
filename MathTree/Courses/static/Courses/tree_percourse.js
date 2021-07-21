function digest_graph_json(json_graph) {

    const pre_nodes = json_graph["nodes"]
    const pre_edges = json_graph["edges"]
    let ord_graph = {"nodes" : [], "edges" : [], "priority" : {}}

    for(let i=0; i < pre_nodes.length; i++) { 
      ord_graph["nodes"].push(pre_nodes[i]["id"]);
      ord_graph["priority"][pre_nodes[i]["id"]] = pre_nodes[i]["y"];
    }

    for(let i=0; i < pre_edges.length; i++) { 
      ord_graph["edges"].push([pre_edges[i]["source"], pre_edges[i]["target"]])
    }

    return ord_graph
}

data = {
    "nodes": [
      {
        "id": "n0",
        "label": "A node",
        "x": 0,
        "y": 0,
        "size": 3
      },
      {
        "id": "n1",
        "label": "Another node",
        "x": 3,
        "y": 1,
        "size": 2
      },
      {
        "id": "n2",
        "label": "And a last one",
        "x": 1,
        "y": 3,
        "size": 1
      }
    ],
    "edges": [
      {
        "id": "e0",
        "source": "n0",
        "target": "n1"
      },
      {
        "id": "e1",
        "source": "n1",
        "target": "n2"
      },
      {
        "id": "e2",
        "source": "n2",
        "target": "n0"
      }
    ]
  }



function tmp_get_percourse(ord_graph, list_prerequisites, current_result, current_node) {
    
    // Current_result must be instanciated as an array containing just the target. 
    // Current_node must be instanciated to just the name of the target.

    for( let i =0 ; i < ord_graph["edges"].length; i++ ) {
        
        if (ord_graph["edges"][i][1] === current_node) {

            if ( (!current_result.includes(ord_graph["edges"][i][0])) && (!list_prerequisites.includes(ord_graph["edges"][i][0])) ) {
                current_result.push(ord_graph["edges"][i][0]);
                tmp_get_percourse(ord_graph, list_prerequisites, current_result, ord_graph["edges"][i][0]);
            }   
        }
    }
}

function get_percourse(ord_graph, list_prerequisites, target) {
    result = [target]
    tmp_get_percourse(ord_graph, list_prerequisites, result, target)
    return result
}

function sort_by_priority(list, priority) {
    
    new_list = [list[0]]

    for(let i =1; i < list.length; i++) {
        
        new_position=0;

        while(priority[list[i]] > priority[new_list[new_position]]) {
            new_position += 1;
        }

        new_list.splice(new_position, 0, list[i])
    }

    return new_list;
}


function get_ordered_path(data, list_prerequisites, target) {
    ord_graph = digest_graph_json(data)
    console.log(ord_graph)
    path = get_percourse(ord_graph, list_prerequisites, target)
    return sort_by_priority(path, ord_graph["priority"])
}
