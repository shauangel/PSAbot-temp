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

// 日期處理 STRAT

// 儲存時，日期轉成字串 傳給後端
function dateToString(datetime){
    var dateTime = new Date(datetime);
    var year = dateTime.getFullYear();
    var month = dateTime.getMonth()+1;//js從0開始取
    var date = dateTime.getDate();
    var hour = dateTime.getHours();
    var minutes = dateTime.getMinutes();
    var second = dateTime.getSeconds();
    var milliSecond = dateTime.getMilliseconds();

    if(month<10){
        month = "0" + month;
    }
    if(date<10){
        date = "0" + date;
    }
    if(hour <10){
        hour = "0" + hour;
    }
    if(minutes <10){
        minutes = "0" + minutes;
    }
    if(second <10){
        second = "0" + second ;
    }

    return year+"-"+month+"-"+date+"T"+hour+":"+minutes+":"+second+"."+milliSecond;
}

// 拿到時，日期轉成JS可用的形式
function dateToJsType(datetime){
    var week = datetime.slice(0, 3); //Wed
    var month = datetime.slice(8, 11); //Aug
    var day = datetime.slice(5, 7); //03
    var year = datetime.slice(12, 16); //2021
    var time = datetime.slice(17, 25); //18:18:38
    
    return week+" "+month+" "+day+" "+year+" "+time+" GMT+0800 (CST)";
}

// 日期處理 END

// 處理textarea裡面 tab的問題 START
$("textarea").keydown(function(e) {
    if(e.keyCode === 9) { // tab was pressed
        // get caret position/selection
        var start = this.selectionStart;
        var end = this.selectionEnd;

        var $this = $(this);
        var value = $this.val();

        // set textarea value to: text before caret + tab + text after caret
        $this.val(value.substring(0, start)
                    + "\t"
                    + value.substring(end));

        // put caret at right position again (add one for the tab)
        this.selectionStart = this.selectionEnd = start + 1;

        // prevent the focus lose
        e.preventDefault();
    }
});
// 處理textarea裡面 tab的問題 END