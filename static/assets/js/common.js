//var head_url = "http://0.0.0.0:55001/api/";
var head_url = "https://soselab.asuscomm.com:55002/api/";

function setPage(page){
    if(page!='comprehensive'){
        localStorage.removeItem("rankId");
    }
    if(page!='summary_new'){
        localStorage.removeItem("summaryId");
    }
    localStorage.setItem("page", page);
}